#
# PySNMP MIB module DOCS-IF-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DOCS-IF-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:52:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
docsIfMib, docsIfCmtsCmStatusEntry = mibBuilder.importSymbols("DOCS-IF-MIB", "docsIfMib", "docsIfCmtsCmStatusEntry")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Bits, MibIdentifier, iso, Unsigned32, ModuleIdentity, ObjectIdentity, Counter64, Counter32, NotificationType, Gauge32, IpAddress, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibIdentifier", "iso", "Unsigned32", "ModuleIdentity", "ObjectIdentity", "Counter64", "Counter32", "NotificationType", "Gauge32", "IpAddress", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
docsIfExtMib = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 127, 21))
docsIfExtMib.setRevisions(('1900-10-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: docsIfExtMib.setRevisionsDescriptions(('Initial Version. ',))
if mibBuilder.loadTexts: docsIfExtMib.setLastUpdated('0011160000Z')
if mibBuilder.loadTexts: docsIfExtMib.setOrganization('IETF IPCDN Working Group')
if mibBuilder.loadTexts: docsIfExtMib.setContactInfo(' ')
if mibBuilder.loadTexts: docsIfExtMib.setDescription('This is the extension Module to rfc2670 DOCS-IF-MIB.')
class DocsisVersion(TextualConvention, Integer32):
    description = 'Indicates the docsis version number.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("docsis10", 1), ("docsis11", 2))

docsIfDocsisCapability = MibScalar((1, 3, 6, 1, 2, 1, 10, 127, 21, 1), DocsisVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsIfDocsisCapability.setStatus('current')
if mibBuilder.loadTexts: docsIfDocsisCapability.setDescription('Indication of the DOCSIS capability of the device.')
docsIfDocsisOperMode = MibScalar((1, 3, 6, 1, 2, 1, 10, 127, 21, 2), DocsisVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsIfDocsisOperMode.setStatus('current')
if mibBuilder.loadTexts: docsIfDocsisOperMode.setDescription('Indication whether the device has registered as a 1.0 or 1.1. For CMTS and unregistered CM, it is always the same as docsDocsisCapability.')
docsIfCmtsCmStatusExtTable = MibTable((1, 3, 6, 1, 2, 1, 10, 127, 21, 3), )
if mibBuilder.loadTexts: docsIfCmtsCmStatusExtTable.setStatus('current')
if mibBuilder.loadTexts: docsIfCmtsCmStatusExtTable.setDescription('A set of objects in the CMTS, maintained for each Cable Modem connected to this CMTS.')
docsIfCmtsCmStatusExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 127, 21, 3, 1), )
docsIfCmtsCmStatusEntry.registerAugmentions(("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusExtEntry"))
docsIfCmtsCmStatusExtEntry.setIndexNames(*docsIfCmtsCmStatusEntry.getIndexNames())
if mibBuilder.loadTexts: docsIfCmtsCmStatusExtEntry.setStatus('current')
if mibBuilder.loadTexts: docsIfCmtsCmStatusExtEntry.setDescription('Status information for a single Cable Modem. An entry in this table exists for each Cable Modem which is connected to the CMTS.')
docsIfCmtsCmStatusDocsisMode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 21, 3, 1, 1), DocsisVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsIfCmtsCmStatusDocsisMode.setStatus('current')
if mibBuilder.loadTexts: docsIfCmtsCmStatusDocsisMode.setDescription('Indication whether the CM has registered as a 1.0 or 1.1 modem')
docsIfExtConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 127, 21, 4))
docsIfExtCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 127, 21, 4, 1))
docsIfExtGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 127, 21, 4, 2))
docsIfExtCmCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 127, 21, 4, 1, 1)).setObjects(("DOCS-IF-EXT-MIB", "docsIfDocsisVersionGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsIfExtCmCompliance = docsIfExtCmCompliance.setStatus('current')
if mibBuilder.loadTexts: docsIfExtCmCompliance.setDescription('The compliance statement.')
docsIfDocsisVersionGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 127, 21, 4, 2, 1)).setObjects(("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsIfDocsisVersionGroup = docsIfDocsisVersionGroup.setStatus('current')
if mibBuilder.loadTexts: docsIfDocsisVersionGroup.setDescription('Object group to indicates DOCSIS version.')
docsIfExtCmtsCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 127, 21, 4, 1, 2)).setObjects(("DOCS-IF-EXT-MIB", "docsIfExtGroup"), ("DOCS-IF-EXT-MIB", "docsIfDocsisVersionGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsIfExtCmtsCompliance = docsIfExtCmtsCompliance.setStatus('current')
if mibBuilder.loadTexts: docsIfExtCmtsCompliance.setDescription('The compliance statement.')
docsIfExtGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 127, 21, 4, 2, 2)).setObjects(("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsIfExtGroup = docsIfExtGroup.setStatus('current')
if mibBuilder.loadTexts: docsIfExtGroup.setDescription('Mandatory implementation group for CMTS.')
mibBuilder.exportSymbols("DOCS-IF-EXT-MIB", docsIfExtConformance=docsIfExtConformance, docsIfDocsisCapability=docsIfDocsisCapability, docsIfExtMib=docsIfExtMib, docsIfDocsisOperMode=docsIfDocsisOperMode, docsIfExtCompliances=docsIfExtCompliances, docsIfDocsisVersionGroup=docsIfDocsisVersionGroup, PYSNMP_MODULE_ID=docsIfExtMib, docsIfExtCmCompliance=docsIfExtCmCompliance, docsIfExtGroups=docsIfExtGroups, docsIfExtCmtsCompliance=docsIfExtCmtsCompliance, docsIfCmtsCmStatusDocsisMode=docsIfCmtsCmStatusDocsisMode, DocsisVersion=DocsisVersion, docsIfExtGroup=docsIfExtGroup, docsIfCmtsCmStatusExtEntry=docsIfCmtsCmStatusExtEntry, docsIfCmtsCmStatusExtTable=docsIfCmtsCmStatusExtTable)
