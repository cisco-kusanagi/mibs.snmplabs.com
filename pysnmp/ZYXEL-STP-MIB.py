#
# PySNMP MIB module ZYXEL-STP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-STP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:45:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Unsigned32, Counter64, iso, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, MibIdentifier, ObjectIdentity, IpAddress, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "Counter64", "iso", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "MibIdentifier", "ObjectIdentity", "IpAddress", "Bits", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelStp = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 79))
if mibBuilder.loadTexts: zyxelStp.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelStp.setOrganization('Enterprise Solution ZyXEL')
zyxelStpSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 79, 1))
zyStpMode = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 79, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("rstp", 1), ("mrstp", 2), ("mstp", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyStpMode.setStatus('current')
zyStpRstpState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 79, 1, 2), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyStpRstpState.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-STP-MIB", zyStpRstpState=zyStpRstpState, zyStpMode=zyStpMode, zyxelStp=zyxelStp, zyxelStpSetup=zyxelStpSetup, PYSNMP_MODULE_ID=zyxelStp)
