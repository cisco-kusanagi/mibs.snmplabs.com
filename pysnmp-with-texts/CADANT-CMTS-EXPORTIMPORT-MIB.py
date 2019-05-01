#
# PySNMP MIB module CADANT-CMTS-EXPORTIMPORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CADANT-CMTS-EXPORTIMPORT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:44:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
trapSeverity, trapCounter = mibBuilder.importSymbols("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity", "trapCounter")
cadExperimental, = mibBuilder.importSymbols("CADANT-PRODUCTS-MIB", "cadExperimental")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Bits, Counter32, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, ModuleIdentity, ObjectIdentity, NotificationType, IpAddress, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "Counter32", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "ModuleIdentity", "ObjectIdentity", "NotificationType", "IpAddress", "TimeTicks", "Unsigned32")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
cadExportImportMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1))
cadExportImportMib.setRevisions(('2001-03-09 00:00', '2004-02-13 00:00', '2004-02-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cadExportImportMib.setRevisionsDescriptions(('Created.', 'Added cadCmtsExportImportWithLineNums, cadCmtsExportImportWithDefaults, cadCmtsExportImportNested, and cadCmtsExportImportWithCertificates.', 'Added cadCmtsExportImportIfIndex',))
if mibBuilder.loadTexts: cadExportImportMib.setLastUpdated('200402160000Z')
if mibBuilder.loadTexts: cadExportImportMib.setOrganization('Arris International Inc.')
if mibBuilder.loadTexts: cadExportImportMib.setContactInfo('Email: support@arrisi.com')
if mibBuilder.loadTexts: cadExportImportMib.setDescription('This MIB defines object which are used to control and report on the exporting and importing of MIB configuration data in the Cadant C4 CMTS.')
class ExportImportAction(TextualConvention, Integer32):
    description = ' Upon reading, this object always returns noop(0). If set to noop(0), no action is taken. If set to export(1), all of the configuraton data in the MIB will be written to the specified file. If set to import(2), the specified file is read in as configuration data.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("noop", 0), ("export", 1), ("import", 2), ("pCmCertExport", 3), ("caCertExport", 4))

class ExportResult(TextualConvention, Integer32):
    description = ' The status of the last export operation. The value of unknown is used upon system initialization.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 0), ("success", 1), ("fileNameTooLong", 2), ("invalidCharactersInFilename", 3), ("fileSystemFull", 4), ("otherError", 5))

class ImportResult(TextualConvention, Integer32):
    description = ' The status of the last import operation. The value of unknown is used upon system initialization.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("success", 1), ("fileNotFound", 2), ("fileDecodingError", 3), ("otherError", 4))

cadCmtsExportImportGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 1))
cadCmtsExportImportFilename = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 1, 1), DisplayString().clone('update:/export.txt')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadCmtsExportImportFilename.setStatus('current')
if mibBuilder.loadTexts: cadCmtsExportImportFilename.setDescription(' The filename to which the MIB configuration data will be written to.')
cadCmtsExportImportAction = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 1, 2), ExportImportAction().clone('noop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadCmtsExportImportAction.setStatus('current')
if mibBuilder.loadTexts: cadCmtsExportImportAction.setDescription(' A cadCmtsExportNotification is sent when an export operation has completed. A cadCmtsImportNotification is sent when an import operation has completed.')
cadCmtsExportResult = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 1, 3), ExportResult().clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadCmtsExportResult.setStatus('current')
if mibBuilder.loadTexts: cadCmtsExportResult.setDescription(' The status of the last export operation. The value of unknown is used upon system initialization.')
cadCmtsImportResult = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 1, 4), ImportResult().clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadCmtsImportResult.setStatus('current')
if mibBuilder.loadTexts: cadCmtsImportResult.setDescription(' The status of the last import operation. The value of unknown is used upon system initialization.')
cadCmtsExportImportWithLineNums = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadCmtsExportImportWithLineNums.setStatus('current')
if mibBuilder.loadTexts: cadCmtsExportImportWithLineNums.setDescription(' If set to true(1) at the time when CadCmtsExportImportAction causes output to be generated, then each line of the output will be prepended with its line number. Note that this output cannot then be put back into the CLI and processed. The line numbers are not valid CLI syntax. Otherwise, if false(2), then output is normal without numbers.')
cadCmtsExportImportWithDefaults = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 1, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadCmtsExportImportWithDefaults.setStatus('current')
if mibBuilder.loadTexts: cadCmtsExportImportWithDefaults.setDescription(' If set to true(1) at the time when CadCmtsExportImportAction causes output to be generated, then all configuration objects are exported, even the ones with default values or otherwise untouched. Otherwise, if false(2), then output is abbreviated and only includes values which are different from their default values or are otherwise difficult to disinguish from their default values.')
cadCmtsExportImportNested = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 1, 7), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadCmtsExportImportNested.setStatus('current')
if mibBuilder.loadTexts: cadCmtsExportImportNested.setDescription(' If set to true(1) at the time when CadCmtsExportImportAction causes output to be generated, then output is grouped in a nested, modal style and contains fewer characters, though a greater number of lines. Otherwise, if false(2), then each output line is fully qualified and capable of being put into a CLI session as-is.')
cadCmtsExportImportWithCertificates = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 1, 8), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadCmtsExportImportWithCertificates.setStatus('current')
if mibBuilder.loadTexts: cadCmtsExportImportWithCertificates.setDescription(' If set to true(1) at the time when CadCmtsExportImportAction causes output to be generated, then output contains BPI+ certificates. Otherwise, if false(2), then output does not contain BPI+ certificates.')
cadCmtsExportImportIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 1, 9), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadCmtsExportImportIfIndex.setStatus('current')
if mibBuilder.loadTexts: cadCmtsExportImportIfIndex.setDescription(' If specified, then only the provisioned information for the specified interface will be exported when cadCmtsExportImportAction is set to true(1). Only cable and fastEthernet interfaces are supported at this time.')
cadCmtsExportImportTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 0))
cadCmtsExportNotification = NotificationType((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 0, 1)).setObjects(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"), ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"), ("CADANT-CMTS-EXPORTIMPORT-MIB", "cadCmtsExportResult"))
if mibBuilder.loadTexts: cadCmtsExportNotification.setStatus('current')
if mibBuilder.loadTexts: cadCmtsExportNotification.setDescription('')
cadCmtsImportNotification = NotificationType((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 1, 0, 2)).setObjects(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"), ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"), ("CADANT-CMTS-EXPORTIMPORT-MIB", "cadCmtsImportResult"))
if mibBuilder.loadTexts: cadCmtsImportNotification.setStatus('current')
if mibBuilder.loadTexts: cadCmtsImportNotification.setDescription('')
mibBuilder.exportSymbols("CADANT-CMTS-EXPORTIMPORT-MIB", cadCmtsImportResult=cadCmtsImportResult, cadExportImportMib=cadExportImportMib, ImportResult=ImportResult, cadCmtsExportImportNested=cadCmtsExportImportNested, cadCmtsExportImportGroup=cadCmtsExportImportGroup, cadCmtsExportImportWithDefaults=cadCmtsExportImportWithDefaults, cadCmtsExportResult=cadCmtsExportResult, cadCmtsExportImportWithCertificates=cadCmtsExportImportWithCertificates, cadCmtsExportImportIfIndex=cadCmtsExportImportIfIndex, ExportResult=ExportResult, cadCmtsExportImportWithLineNums=cadCmtsExportImportWithLineNums, cadCmtsExportImportTraps=cadCmtsExportImportTraps, cadCmtsExportNotification=cadCmtsExportNotification, PYSNMP_MODULE_ID=cadExportImportMib, cadCmtsExportImportFilename=cadCmtsExportImportFilename, cadCmtsExportImportAction=cadCmtsExportImportAction, cadCmtsImportNotification=cadCmtsImportNotification, ExportImportAction=ExportImportAction)
