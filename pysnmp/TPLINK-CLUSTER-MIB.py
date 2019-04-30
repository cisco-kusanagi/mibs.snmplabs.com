#
# PySNMP MIB module TPLINK-CLUSTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-CLUSTER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:16:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Bits, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, Counter64, NotificationType, IpAddress, ObjectIdentity, TimeTicks, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Bits", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "Counter64", "NotificationType", "IpAddress", "ObjectIdentity", "TimeTicks", "Counter32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tplinkClusterMIBObjects, = mibBuilder.importSymbols("TPLINK-CLUSTERTREE-MIB", "tplinkClusterMIBObjects")
tplinkClusterMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1))
tplinkClusterMIB.setRevisions(('2009-08-27 00:00',))
if mibBuilder.loadTexts: tplinkClusterMIB.setLastUpdated('200908270000Z')
if mibBuilder.loadTexts: tplinkClusterMIB.setOrganization('TPLINK')
ndpManage = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 1))
ntdpManage = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 2))
clusterManage = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3))
mibBuilder.exportSymbols("TPLINK-CLUSTER-MIB", tplinkClusterMIB=tplinkClusterMIB, PYSNMP_MODULE_ID=tplinkClusterMIB, clusterManage=clusterManage, ntdpManage=ntdpManage, ndpManage=ndpManage)
