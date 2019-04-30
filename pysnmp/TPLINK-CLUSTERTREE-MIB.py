#
# PySNMP MIB module TPLINK-CLUSTERTREE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-CLUSTERTREE-MIB
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
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkClusterTreeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 33))
tplinkClusterTreeMIB.setRevisions(('2012-12-13 09:30',))
if mibBuilder.loadTexts: tplinkClusterTreeMIB.setLastUpdated('201212130930Z')
if mibBuilder.loadTexts: tplinkClusterTreeMIB.setOrganization('TPLINK')
tplinkClusterMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1))
tplinkClusterNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 33, 2))
mibBuilder.exportSymbols("TPLINK-CLUSTERTREE-MIB", tplinkClusterMIBObjects=tplinkClusterMIBObjects, tplinkClusterNotifications=tplinkClusterNotifications, PYSNMP_MODULE_ID=tplinkClusterTreeMIB, tplinkClusterTreeMIB=tplinkClusterTreeMIB)
