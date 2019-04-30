#
# PySNMP MIB module ZYXEL-IGMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-IGMP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:44:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, IpAddress, Counter32, Counter64, MibIdentifier, TimeTicks, Integer32, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "Counter32", "Counter64", "MibIdentifier", "TimeTicks", "Integer32", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "iso", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyRouteDomainIpAddress, zyRouteDomainIpMaskBits = mibBuilder.importSymbols("ZYXEL-IP-FORWARD-MIB", "zyRouteDomainIpAddress", "zyRouteDomainIpMaskBits")
zyxelIgmp = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 29))
if mibBuilder.loadTexts: zyxelIgmp.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelIgmp.setOrganization('Enterprise Solution ZyXEL')
zyxelIgmpSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 29, 1))
zyIgmpState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 29, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyIgmpState.setStatus('current')
zyxelIgmpRouteDomainTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 29, 1, 2), )
if mibBuilder.loadTexts: zyxelIgmpRouteDomainTable.setStatus('current')
zyxelIgmpRouteDomainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 29, 1, 2, 1), ).setIndexNames((0, "ZYXEL-IP-FORWARD-MIB", "zyRouteDomainIpAddress"), (0, "ZYXEL-IP-FORWARD-MIB", "zyRouteDomainIpMaskBits"))
if mibBuilder.loadTexts: zyxelIgmpRouteDomainEntry.setStatus('current')
zyIgmpRouteDomainVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 29, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("igmpV1", 1), ("igmpV2", 2), ("igmpV3", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyIgmpRouteDomainVersion.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-IGMP-MIB", zyxelIgmpSetup=zyxelIgmpSetup, zyxelIgmp=zyxelIgmp, PYSNMP_MODULE_ID=zyxelIgmp, zyxelIgmpRouteDomainEntry=zyxelIgmpRouteDomainEntry, zyIgmpRouteDomainVersion=zyIgmpRouteDomainVersion, zyIgmpState=zyIgmpState, zyxelIgmpRouteDomainTable=zyxelIgmpRouteDomainTable)
