#
# PySNMP MIB module HP-ICF-DOS-FILTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-DOS-FILTER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:21:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ObjectIdentity, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, Counter64, MibIdentifier, IpAddress, Bits, Unsigned32, iso, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "Counter64", "MibIdentifier", "IpAddress", "Bits", "Unsigned32", "iso", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpicfDosFilterMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60))
hpicfDosFilterMib.setRevisions(('2009-04-03 10:00',))
if mibBuilder.loadTexts: hpicfDosFilterMib.setLastUpdated('200904031000Z')
if mibBuilder.loadTexts: hpicfDosFilterMib.setOrganization('HP Networking')
hpicfDosFilterObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60, 1))
hpicfDosFilterConfig = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDosFilterConfig.setStatus('current')
hpicfDosFilterConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60, 2))
hpicfDosFilterCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60, 2, 1))
hpicfDosFilterGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60, 2, 2))
hpicfDosFilterCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60, 2, 1, 1)).setObjects(("HP-ICF-DOS-FILTER-MIB", "hpicfDosFilterGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDosFilterCompliance = hpicfDosFilterCompliance.setStatus('current')
hpicfDosFilterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60, 2, 2, 1)).setObjects(("HP-ICF-DOS-FILTER-MIB", "hpicfDosFilterConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDosFilterGroup = hpicfDosFilterGroup.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-DOS-FILTER-MIB", PYSNMP_MODULE_ID=hpicfDosFilterMib, hpicfDosFilterConfig=hpicfDosFilterConfig, hpicfDosFilterGroup=hpicfDosFilterGroup, hpicfDosFilterCompliances=hpicfDosFilterCompliances, hpicfDosFilterCompliance=hpicfDosFilterCompliance, hpicfDosFilterGroups=hpicfDosFilterGroups, hpicfDosFilterMib=hpicfDosFilterMib, hpicfDosFilterObjects=hpicfDosFilterObjects, hpicfDosFilterConformance=hpicfDosFilterConformance)
