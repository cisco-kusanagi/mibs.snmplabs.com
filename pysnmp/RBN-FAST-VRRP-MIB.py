#
# PySNMP MIB module RBN-FAST-VRRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-FAST-VRRP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:44:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, Counter64, ObjectIdentity, Gauge32, Unsigned32, Integer32, MibIdentifier, Bits, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "Integer32", "MibIdentifier", "Bits", "IpAddress", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
VrId, = mibBuilder.importSymbols("VRRP-MIB", "VrId")
rbnFastVrrpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 45))
rbnFastVrrpMIB.setRevisions(('2008-05-21 00:00',))
if mibBuilder.loadTexts: rbnFastVrrpMIB.setLastUpdated('200805210000Z')
if mibBuilder.loadTexts: rbnFastVrrpMIB.setOrganization('Redback Networks, Inc.')
rbnFastVrrpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 45, 1))
rbnFastVrrpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 45, 2))
rbnFastVrrpOperTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 45, 1, 1), )
if mibBuilder.loadTexts: rbnFastVrrpOperTable.setStatus('current')
rbnFastVrrpOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 45, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "RBN-FAST-VRRP-MIB", "rbnFastVrrpOperVrId"))
if mibBuilder.loadTexts: rbnFastVrrpOperEntry.setStatus('current')
rbnFastVrrpOperVrId = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 45, 1, 1, 1, 1), VrId())
if mibBuilder.loadTexts: rbnFastVrrpOperVrId.setStatus('current')
rbnFastVrrpOperAdvertisementInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 45, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 999))).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnFastVrrpOperAdvertisementInterval.setStatus('current')
rbnFastVrrpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 45, 2, 1))
rbnFastVrrpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 45, 2, 2))
rbnFastVrrpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 45, 2, 1, 1)).setObjects(("RBN-FAST-VRRP-MIB", "rbnFastVrrpObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnFastVrrpCompliance = rbnFastVrrpCompliance.setStatus('current')
rbnFastVrrpObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 45, 2, 2, 1)).setObjects(("RBN-FAST-VRRP-MIB", "rbnFastVrrpOperAdvertisementInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnFastVrrpObjectGroup = rbnFastVrrpObjectGroup.setStatus('current')
mibBuilder.exportSymbols("RBN-FAST-VRRP-MIB", rbnFastVrrpObjectGroup=rbnFastVrrpObjectGroup, rbnFastVrrpConformance=rbnFastVrrpConformance, PYSNMP_MODULE_ID=rbnFastVrrpMIB, rbnFastVrrpOperVrId=rbnFastVrrpOperVrId, rbnFastVrrpOperAdvertisementInterval=rbnFastVrrpOperAdvertisementInterval, rbnFastVrrpMIBGroups=rbnFastVrrpMIBGroups, rbnFastVrrpCompliance=rbnFastVrrpCompliance, rbnFastVrrpMIBObjects=rbnFastVrrpMIBObjects, rbnFastVrrpOperEntry=rbnFastVrrpOperEntry, rbnFastVrrpOperTable=rbnFastVrrpOperTable, rbnFastVrrpMIBCompliances=rbnFastVrrpMIBCompliances, rbnFastVrrpMIB=rbnFastVrrpMIB)
