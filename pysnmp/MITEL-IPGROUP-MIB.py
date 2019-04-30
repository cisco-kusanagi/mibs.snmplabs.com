#
# PySNMP MIB module MITEL-IPGROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MITEL-IPGROUP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:03:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, Gauge32, enterprises, ModuleIdentity, Counter64, IpAddress, Bits, MibIdentifier, TimeTicks, Counter32, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "Gauge32", "enterprises", "ModuleIdentity", "Counter64", "IpAddress", "Bits", "MibIdentifier", "TimeTicks", "Counter32", "NotificationType", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mitelRouterIpGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1))
mitelRouterIpGroup.setRevisions(('2003-03-24 09:08', '1999-03-01 00:00',))
if mibBuilder.loadTexts: mitelRouterIpGroup.setLastUpdated('200303240908Z')
if mibBuilder.loadTexts: mitelRouterIpGroup.setOrganization('MITEL Corporation')
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelPropIpNetworking = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8))
mitelIpNetRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1))
mitelIpGrpFilterGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1))
mitelIpGrpNatGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2))
mitelIpGrpDnsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3))
mitelIpGrpIpVirtualGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4))
mitelIpGrpLogicalGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5))
mitelIpGrpBackupWANGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 6))
mibBuilder.exportSymbols("MITEL-IPGROUP-MIB", mitelIpGrpBackupWANGroup=mitelIpGrpBackupWANGroup, PYSNMP_MODULE_ID=mitelRouterIpGroup, mitelProprietary=mitelProprietary, mitelIpGrpNatGroup=mitelIpGrpNatGroup, mitelIpNetRouter=mitelIpNetRouter, mitelRouterIpGroup=mitelRouterIpGroup, mitelIpGrpFilterGroup=mitelIpGrpFilterGroup, mitelIpGrpDnsGroup=mitelIpGrpDnsGroup, mitelIpGrpIpVirtualGroup=mitelIpGrpIpVirtualGroup, mitel=mitel, mitelPropIpNetworking=mitelPropIpNetworking, mitelIpGrpLogicalGroup=mitelIpGrpLogicalGroup)
