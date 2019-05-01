#
# PySNMP MIB module HPICF-ACTIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPICF-ACTIVATE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:37:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
NotificationType, ModuleIdentity, Counter32, Unsigned32, iso, TimeTicks, MibIdentifier, Gauge32, Bits, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "Counter32", "Unsigned32", "iso", "TimeTicks", "MibIdentifier", "Gauge32", "Bits", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
hpicfActivateMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129))
hpicfActivateMIB.setRevisions(('2016-05-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfActivateMIB.setRevisionsDescriptions(('Initial version',))
if mibBuilder.loadTexts: hpicfActivateMIB.setLastUpdated('201605030000Z')
if mibBuilder.loadTexts: hpicfActivateMIB.setOrganization('HPE Networking')
if mibBuilder.loadTexts: hpicfActivateMIB.setContactInfo('Hewlett Packard Enterprise Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfActivateMIB.setDescription('This MIB defines HPE proprietary objects used to configure the Activate feature.')
hpicfActivateObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 1))
hpicfActivateConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 2))
hpicfActivateSoftwareUpdateMode = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfActivateSoftwareUpdateMode.setStatus('current')
if mibBuilder.loadTexts: hpicfActivateSoftwareUpdateMode.setDescription('Enable polling the Aruba Activate server for software updates.')
hpicfActivateProvisionMode = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 1, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfActivateProvisionMode.setStatus('current')
if mibBuilder.loadTexts: hpicfActivateProvisionMode.setDescription('Enable Activate provision service.')
hpicfActivateMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 2, 1))
hpicfActivateMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 2, 2))
hpicfActivateMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 2, 1, 1)).setObjects(("HPICF-ACTIVATE-MIB", "hpicfActivateConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfActivateMIBCompliance = hpicfActivateMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: hpicfActivateMIBCompliance.setDescription('The compliance statement for HPE switches implementing the HPICF-Activate MIB.')
hpicfActivateConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 2, 2, 1)).setObjects(("HPICF-ACTIVATE-MIB", "hpicfActivateSoftwareUpdateMode"), ("HPICF-ACTIVATE-MIB", "hpicfActivateProvisionMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfActivateConfigGroup = hpicfActivateConfigGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfActivateConfigGroup.setDescription('A collection of objects to support the Activate feature.')
mibBuilder.exportSymbols("HPICF-ACTIVATE-MIB", hpicfActivateMIB=hpicfActivateMIB, hpicfActivateConfigGroup=hpicfActivateConfigGroup, PYSNMP_MODULE_ID=hpicfActivateMIB, hpicfActivateMIBCompliance=hpicfActivateMIBCompliance, hpicfActivateMIBCompliances=hpicfActivateMIBCompliances, hpicfActivateObjects=hpicfActivateObjects, hpicfActivateMIBGroups=hpicfActivateMIBGroups, hpicfActivateProvisionMode=hpicfActivateProvisionMode, hpicfActivateConformance=hpicfActivateConformance, hpicfActivateSoftwareUpdateMode=hpicfActivateSoftwareUpdateMode)
