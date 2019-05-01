#
# PySNMP MIB module ZYXEL-STP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-STP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:51:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Unsigned32, Bits, IpAddress, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, Counter64, MibIdentifier, NotificationType, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "Bits", "IpAddress", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "Counter64", "MibIdentifier", "NotificationType", "TimeTicks", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelStp = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 79))
if mibBuilder.loadTexts: zyxelStp.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelStp.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: zyxelStp.setContactInfo('')
if mibBuilder.loadTexts: zyxelStp.setDescription('The subtree for Spanning Tree Protocol (STP)')
zyxelStpSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 79, 1))
zyStpMode = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 79, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("rstp", 1), ("mrstp", 2), ("mstp", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyStpMode.setStatus('current')
if mibBuilder.loadTexts: zyStpMode.setDescription('Activate one of the spanning tree protocol modes on the Switch. ')
zyStpRstpState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 79, 1, 2), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyStpRstpState.setStatus('current')
if mibBuilder.loadTexts: zyStpRstpState.setDescription('Enable/Disable rapid spanning tree protocol. You must also activate rapid spanning tree protocol mode on the switch.')
mibBuilder.exportSymbols("ZYXEL-STP-MIB", zyStpMode=zyStpMode, zyStpRstpState=zyStpRstpState, PYSNMP_MODULE_ID=zyxelStp, zyxelStpSetup=zyxelStpSetup, zyxelStp=zyxelStp)
