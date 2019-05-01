#
# PySNMP MIB module TPLINK-CLUSTERTREE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-CLUSTERTREE-MIB
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
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkClusterTreeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 33))
tplinkClusterTreeMIB.setRevisions(('2012-12-13 09:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tplinkClusterTreeMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: tplinkClusterTreeMIB.setLastUpdated('201212130930Z')
if mibBuilder.loadTexts: tplinkClusterTreeMIB.setOrganization('TPLINK')
if mibBuilder.loadTexts: tplinkClusterTreeMIB.setContactInfo('www.tplink.com.cn')
if mibBuilder.loadTexts: tplinkClusterTreeMIB.setDescription('Private MIB for Cluster.')
tplinkClusterMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1))
tplinkClusterNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 33, 2))
mibBuilder.exportSymbols("TPLINK-CLUSTERTREE-MIB", tplinkClusterMIBObjects=tplinkClusterMIBObjects, PYSNMP_MODULE_ID=tplinkClusterTreeMIB, tplinkClusterTreeMIB=tplinkClusterTreeMIB, tplinkClusterNotifications=tplinkClusterNotifications)
