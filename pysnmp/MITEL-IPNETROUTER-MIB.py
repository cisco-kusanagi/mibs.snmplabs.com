#
# PySNMP MIB module MITEL-IPNETROUTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MITEL-IPNETROUTER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:03:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ObjectIdentity, Integer32, IpAddress, enterprises, NotificationType, MibIdentifier, Unsigned32, TimeTicks, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "Integer32", "IpAddress", "enterprises", "NotificationType", "MibIdentifier", "Unsigned32", "TimeTicks", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mitelIpNetRouter = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1))
mitelIpNetRouter.setRevisions(('2003-03-24 09:27', '1999-03-01 00:00',))
if mibBuilder.loadTexts: mitelIpNetRouter.setLastUpdated('200303240927Z')
if mibBuilder.loadTexts: mitelIpNetRouter.setOrganization('MITEL Corporation')
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelPropIpNetworking = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8))
mitelRouterIpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1))
mitelRouterPppGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 2))
mitelRouterDhcpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3))
mitelRouterLogicalGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4))
mitelRouterIpRouterGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5))
mitelRouterRipExtensionGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 6))
mitelRouterSnmpTrapGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 7))
mibBuilder.exportSymbols("MITEL-IPNETROUTER-MIB", mitelRouterDhcpGroup=mitelRouterDhcpGroup, mitelProprietary=mitelProprietary, PYSNMP_MODULE_ID=mitelIpNetRouter, mitelRouterRipExtensionGroup=mitelRouterRipExtensionGroup, mitelRouterSnmpTrapGroup=mitelRouterSnmpTrapGroup, mitelRouterPppGroup=mitelRouterPppGroup, mitelIpNetRouter=mitelIpNetRouter, mitelRouterIpRouterGroup=mitelRouterIpRouterGroup, mitel=mitel, mitelRouterIpGroup=mitelRouterIpGroup, mitelPropIpNetworking=mitelPropIpNetworking, mitelRouterLogicalGroup=mitelRouterLogicalGroup)
