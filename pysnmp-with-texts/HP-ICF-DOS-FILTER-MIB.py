#
# PySNMP MIB module HP-ICF-DOS-FILTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-DOS-FILTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:33:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, Counter64, NotificationType, IpAddress, Bits, ObjectIdentity, Unsigned32, Counter32, MibIdentifier, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "Counter64", "NotificationType", "IpAddress", "Bits", "ObjectIdentity", "Unsigned32", "Counter32", "MibIdentifier", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpicfDosFilterMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60))
hpicfDosFilterMib.setRevisions(('2009-04-03 10:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfDosFilterMib.setRevisionsDescriptions(('Initial version',))
if mibBuilder.loadTexts: hpicfDosFilterMib.setLastUpdated('200904031000Z')
if mibBuilder.loadTexts: hpicfDosFilterMib.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpicfDosFilterMib.setContactInfo('Hewlett Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfDosFilterMib.setDescription('This MIB describes objects for management of Denial of Service (DoS) attack packet filtering.')
hpicfDosFilterObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60, 1))
hpicfDosFilterConfig = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDosFilterConfig.setStatus('current')
if mibBuilder.loadTexts: hpicfDosFilterConfig.setDescription('This object enables Denial of Service (DoS) packet filtering. When enabled, the device will automatically discard packets that match certain DoS attack profiles.')
hpicfDosFilterConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60, 2))
hpicfDosFilterCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60, 2, 1))
hpicfDosFilterGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60, 2, 2))
hpicfDosFilterCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60, 2, 1, 1)).setObjects(("HP-ICF-DOS-FILTER-MIB", "hpicfDosFilterGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDosFilterCompliance = hpicfDosFilterCompliance.setStatus('current')
if mibBuilder.loadTexts: hpicfDosFilterCompliance.setDescription('Describes the requirements for conformance to the DosFilter MIB.')
hpicfDosFilterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60, 2, 2, 1)).setObjects(("HP-ICF-DOS-FILTER-MIB", "hpicfDosFilterConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDosFilterGroup = hpicfDosFilterGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfDosFilterGroup.setDescription('DosFilter objects.')
mibBuilder.exportSymbols("HP-ICF-DOS-FILTER-MIB", PYSNMP_MODULE_ID=hpicfDosFilterMib, hpicfDosFilterConfig=hpicfDosFilterConfig, hpicfDosFilterCompliance=hpicfDosFilterCompliance, hpicfDosFilterMib=hpicfDosFilterMib, hpicfDosFilterObjects=hpicfDosFilterObjects, hpicfDosFilterGroups=hpicfDosFilterGroups, hpicfDosFilterGroup=hpicfDosFilterGroup, hpicfDosFilterConformance=hpicfDosFilterConformance, hpicfDosFilterCompliances=hpicfDosFilterCompliances)
