#
# PySNMP MIB module TPLINK-CLUSTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-CLUSTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:24:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Unsigned32, Counter32, MibIdentifier, iso, ObjectIdentity, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, Bits, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "Counter32", "MibIdentifier", "iso", "ObjectIdentity", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "Bits", "Integer32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkClusterMIBObjects, = mibBuilder.importSymbols("TPLINK-CLUSTERTREE-MIB", "tplinkClusterMIBObjects")
tplinkClusterMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1))
tplinkClusterMIB.setRevisions(('2009-08-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tplinkClusterMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: tplinkClusterMIB.setLastUpdated('200908270000Z')
if mibBuilder.loadTexts: tplinkClusterMIB.setOrganization('TPLINK')
if mibBuilder.loadTexts: tplinkClusterMIB.setContactInfo('www.tplink.com.cn')
if mibBuilder.loadTexts: tplinkClusterMIB.setDescription('Cluster Management function enables a network administer to manage the scattered devices in the network via a management device. After a commander switch is configured, management and maintenance operations intended for the member devices in a cluster is implemented by the commander device. ')
ndpManage = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 1))
ntdpManage = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 2))
clusterManage = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3))
mibBuilder.exportSymbols("TPLINK-CLUSTER-MIB", clusterManage=clusterManage, tplinkClusterMIB=tplinkClusterMIB, ndpManage=ndpManage, ntdpManage=ntdpManage, PYSNMP_MODULE_ID=tplinkClusterMIB)
