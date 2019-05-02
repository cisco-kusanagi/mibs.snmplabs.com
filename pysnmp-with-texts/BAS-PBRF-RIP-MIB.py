#
# PySNMP MIB module BAS-PBRF-RIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAS-PBRF-RIP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:34:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
BasSlotId, BasInterfaceId, basPbrfRIP, BasLogicalPortId, BasChassisId = mibBuilder.importSymbols("BAS-MIB", "BasSlotId", "BasInterfaceId", "basPbrfRIP", "BasLogicalPortId", "BasChassisId")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, IpAddress, Integer32, Bits, TimeTicks, Gauge32, ObjectIdentity, iso, Unsigned32, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "Integer32", "Bits", "TimeTicks", "Gauge32", "ObjectIdentity", "iso", "Unsigned32", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
basPbrfRIPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1))
if mibBuilder.loadTexts: basPbrfRIPMIB.setLastUpdated('9812220800Z')
if mibBuilder.loadTexts: basPbrfRIPMIB.setOrganization('Broadband Access Systems, Inc.')
if mibBuilder.loadTexts: basPbrfRIPMIB.setContactInfo(' Tech Support Broadband Access Systems, Inc. 201 Forest Street Marlborough, MA 01752 USA 508-485-8200 support@basystems.com')
if mibBuilder.loadTexts: basPbrfRIPMIB.setDescription('The MIB module defines the configuration MIB objects for Broadband Access Systems, Inc. RIP Export policy based routing filters.')
basPbrfRIPImport = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1))
basPbrfRIPExport = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2))
basPbrfRIPImportTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 1), )
if mibBuilder.loadTexts: basPbrfRIPImportTable.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportTable.setDescription('A table of RIP import PBRF test filter entries.')
basPbrfRIPImportEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 1, 1), ).setIndexNames((0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportChassis"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportSlot"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportIf"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportLPort"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportIndex"))
if mibBuilder.loadTexts: basPbrfRIPImportEntry.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportEntry.setDescription('An entry containing management information applicable to an RIP import PBRF filter used for testing the validity of a filter.')
basPbrfRIPImportChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 1, 1, 1), BasChassisId())
if mibBuilder.loadTexts: basPbrfRIPImportChassis.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportChassis.setDescription('The chassis identifier of this chassis.')
basPbrfRIPImportSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 1, 1, 2), BasSlotId())
if mibBuilder.loadTexts: basPbrfRIPImportSlot.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportSlot.setDescription('The BAS slot ID of this card.')
basPbrfRIPImportIf = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 1, 1, 3), BasInterfaceId())
if mibBuilder.loadTexts: basPbrfRIPImportIf.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportIf.setDescription('The BAS interface ID of this card.')
basPbrfRIPImportLPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 1, 1, 4), BasLogicalPortId())
if mibBuilder.loadTexts: basPbrfRIPImportLPort.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportLPort.setDescription('The BAS logical port ID of this card.')
basPbrfRIPImportIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 1, 1, 5), Integer32())
if mibBuilder.loadTexts: basPbrfRIPImportIndex.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportIndex.setDescription('The index of the filter.')
basPbrfRIPImportTemplateCount = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basPbrfRIPImportTemplateCount.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportTemplateCount.setDescription('The number of templates assigned to this filter.')
basPbrfRIPImportRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportRowStatus.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportRowStatus.setDescription('The row status of the filter.')
basPbrfRIPImportDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportDescr.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportDescr.setDescription('The descr of the RIP Import.')
basPbrfRIPImportFilterTempTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 2), )
if mibBuilder.loadTexts: basPbrfRIPImportFilterTempTable.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportFilterTempTable.setDescription('A table of RIP import PBRF filters.')
basPbrfRIPImportFilterTempEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 2, 1), ).setIndexNames((0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportFilterTempChassis"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportFilterTempSlot"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportFilterTempIf"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportFilterTempLPort"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportFilterTempIndex"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportFilterTempTemplate"))
if mibBuilder.loadTexts: basPbrfRIPImportFilterTempEntry.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportFilterTempEntry.setDescription('An entry containing management information applicable to a RIP import PBRF filter.')
basPbrfRIPImportFilterTempChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 2, 1, 1), BasChassisId())
if mibBuilder.loadTexts: basPbrfRIPImportFilterTempChassis.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportFilterTempChassis.setDescription('The BAS chassis identifier of this chassis.')
basPbrfRIPImportFilterTempSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 2, 1, 2), BasSlotId())
if mibBuilder.loadTexts: basPbrfRIPImportFilterTempSlot.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportFilterTempSlot.setDescription('The BAS slot ID of this card.')
basPbrfRIPImportFilterTempIf = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 2, 1, 3), BasInterfaceId())
if mibBuilder.loadTexts: basPbrfRIPImportFilterTempIf.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportFilterTempIf.setDescription('The BAS interface ID of this card.')
basPbrfRIPImportFilterTempLPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 2, 1, 4), BasLogicalPortId())
if mibBuilder.loadTexts: basPbrfRIPImportFilterTempLPort.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportFilterTempLPort.setDescription('The BAS logical port ID of this card.')
basPbrfRIPImportFilterTempIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 2, 1, 5), Integer32())
if mibBuilder.loadTexts: basPbrfRIPImportFilterTempIndex.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportFilterTempIndex.setDescription('The index of the filter.')
basPbrfRIPImportFilterTempTemplate = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 2, 1, 6), Integer32())
if mibBuilder.loadTexts: basPbrfRIPImportFilterTempTemplate.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportFilterTempTemplate.setDescription('The index for the specific template.')
basPbrfRIPImportFilterTempOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 2, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportFilterTempOrder.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportFilterTempOrder.setDescription('The order in which the template is applied.')
basPbrfRIPImportFilterTempRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 2, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportFilterTempRowStatus.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportFilterTempRowStatus.setDescription('The row status of the filter.')
basPbrfRIPImportTemplateTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3), )
if mibBuilder.loadTexts: basPbrfRIPImportTemplateTable.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportTemplateTable.setDescription('A table of RIP Import template entries.')
basPbrfRIPImportTemplateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1), ).setIndexNames((0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportTemplateChassis"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportTemplateSlot"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportTemplateIf"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportTemplateLPort"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportTemplateIndex"))
if mibBuilder.loadTexts: basPbrfRIPImportTemplateEntry.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportTemplateEntry.setDescription('An entry containing management information applicable to a RIP Import PBRF template.')
basPbrfRIPImportTemplateChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 1), BasChassisId())
if mibBuilder.loadTexts: basPbrfRIPImportTemplateChassis.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportTemplateChassis.setDescription('The BAS chassis identifier of this chassis.')
basPbrfRIPImportTemplateSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 2), BasSlotId())
if mibBuilder.loadTexts: basPbrfRIPImportTemplateSlot.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportTemplateSlot.setDescription('The BAS slot ID of this card.')
basPbrfRIPImportTemplateIf = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 3), BasInterfaceId())
if mibBuilder.loadTexts: basPbrfRIPImportTemplateIf.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportTemplateIf.setDescription('The BAS interface ID of this card.')
basPbrfRIPImportTemplateLPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 4), BasLogicalPortId())
if mibBuilder.loadTexts: basPbrfRIPImportTemplateLPort.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportTemplateLPort.setDescription('The BAS logical port ID of this card.')
basPbrfRIPImportTemplateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 5), Integer32())
if mibBuilder.loadTexts: basPbrfRIPImportTemplateIndex.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportTemplateIndex.setDescription('The index of the template.')
basPbrfRIPImportTemplateRouteAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 6), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportTemplateRouteAddr.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportTemplateRouteAddr.setDescription('The Route Address key of the template.')
basPbrfRIPImportTemplateRouteMask = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 7), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportTemplateRouteMask.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportTemplateRouteMask.setDescription('The Route Mask key of the template.')
basPbrfRIPImportTemplatePeerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 8), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportTemplatePeerAddr.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportTemplatePeerAddr.setDescription('The PeerAddr key of the template.')
basPbrfRIPImportTemplatePeerMask = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 9), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportTemplatePeerMask.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportTemplatePeerMask.setDescription('The PeerMask key of the template.')
basPbrfRIPImportTemplateTag = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 10), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportTemplateTag.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportTemplateTag.setDescription('The tag key of the template.')
basPbrfRIPImportTemplateKeyBits = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 11), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportTemplateKeyBits.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportTemplateKeyBits.setDescription('The key bits key mask of the template.')
basPbrfRIPImportTemplatePref = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 12), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportTemplatePref.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportTemplatePref.setDescription('The preference of the template action.')
basPbrfRIPImportTemplateMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 13), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportTemplateMetric.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportTemplateMetric.setDescription('The metric of the template action.')
basPbrfRIPImportTemplateFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 14), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportTemplateFlags.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportTemplateFlags.setDescription('The flags of the template action.')
basPbrfRIPImportTemplateActionTag = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 15), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportTemplateActionTag.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportTemplateActionTag.setDescription('The tag of the template action.')
basPbrfRIPImportTemplateRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 16), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportTemplateRowStatus.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportTemplateRowStatus.setDescription('The row status of the template.')
basPbrfRIPImportTemplateDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 17), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPImportTemplateDescr.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPImportTemplateDescr.setDescription('The descr of the RIP Import template.')
basPbrfRIPExportTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 1), )
if mibBuilder.loadTexts: basPbrfRIPExportTable.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportTable.setDescription('A table of RIP export PBRF test filter entries.')
basPbrfRIPExportEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 1, 1), ).setIndexNames((0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportChassis"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportSlot"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportIf"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportLPort"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportIndex"))
if mibBuilder.loadTexts: basPbrfRIPExportEntry.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportEntry.setDescription('An entry containing management information applicable to an RIP export PBRF filter used for testing the validity of a filter.')
basPbrfRIPExportChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 1, 1, 1), BasChassisId())
if mibBuilder.loadTexts: basPbrfRIPExportChassis.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportChassis.setDescription('The chassis identifier of this chassis.')
basPbrfRIPExportSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 1, 1, 2), BasSlotId())
if mibBuilder.loadTexts: basPbrfRIPExportSlot.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportSlot.setDescription('The BAS slot ID of this card.')
basPbrfRIPExportIf = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 1, 1, 3), BasInterfaceId())
if mibBuilder.loadTexts: basPbrfRIPExportIf.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportIf.setDescription('The BAS interface ID of this card.')
basPbrfRIPExportLPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 1, 1, 4), BasLogicalPortId())
if mibBuilder.loadTexts: basPbrfRIPExportLPort.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportLPort.setDescription('The BAS logical port ID of this card.')
basPbrfRIPExportIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 1, 1, 5), Integer32())
if mibBuilder.loadTexts: basPbrfRIPExportIndex.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportIndex.setDescription('The index of the filter.')
basPbrfRIPExportTemplateCount = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basPbrfRIPExportTemplateCount.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportTemplateCount.setDescription('The number of templates assigned to this filter.')
basPbrfRIPExportRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportRowStatus.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportRowStatus.setDescription('The row status of the filter.')
basPbrfRIPExportDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportDescr.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportDescr.setDescription('The descr of the RIP Export.')
basPbrfRIPExportFilterTempTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 2), )
if mibBuilder.loadTexts: basPbrfRIPExportFilterTempTable.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportFilterTempTable.setDescription('A table of RIP Export PBRF filter/template bindings.')
basPbrfRIPExportFilterTempEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 2, 1), ).setIndexNames((0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportFilterTempChassis"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportFilterTempSlot"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportFilterTempIf"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportFilterTempLPort"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportFilterTempIndex"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportFilterTempTemplate"))
if mibBuilder.loadTexts: basPbrfRIPExportFilterTempEntry.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportFilterTempEntry.setDescription('An entry containing management information applicable to a RIP export PBRF filter.')
basPbrfRIPExportFilterTempChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 2, 1, 1), BasChassisId())
if mibBuilder.loadTexts: basPbrfRIPExportFilterTempChassis.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportFilterTempChassis.setDescription('The BAS chassis identifier of this chassis.')
basPbrfRIPExportFilterTempSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 2, 1, 2), BasSlotId())
if mibBuilder.loadTexts: basPbrfRIPExportFilterTempSlot.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportFilterTempSlot.setDescription('The BAS slot ID of this card.')
basPbrfRIPExportFilterTempIf = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 2, 1, 3), BasInterfaceId())
if mibBuilder.loadTexts: basPbrfRIPExportFilterTempIf.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportFilterTempIf.setDescription('The BAS interface ID of this card.')
basPbrfRIPExportFilterTempLPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 2, 1, 4), BasLogicalPortId())
if mibBuilder.loadTexts: basPbrfRIPExportFilterTempLPort.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportFilterTempLPort.setDescription('The BAS logical port ID of this card.')
basPbrfRIPExportFilterTempIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 2, 1, 5), Integer32())
if mibBuilder.loadTexts: basPbrfRIPExportFilterTempIndex.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportFilterTempIndex.setDescription('The index of the filter.')
basPbrfRIPExportFilterTempTemplate = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 2, 1, 6), Integer32())
if mibBuilder.loadTexts: basPbrfRIPExportFilterTempTemplate.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportFilterTempTemplate.setDescription('The index for the specific template.')
basPbrfRIPExportFilterTempOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 2, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportFilterTempOrder.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportFilterTempOrder.setDescription('The order in which the template is applied.')
basPbrfRIPExportFilterTempRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 2, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportFilterTempRowStatus.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportFilterTempRowStatus.setDescription('The row status of the filter.')
basPbrfRIPExportTemplateTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3), )
if mibBuilder.loadTexts: basPbrfRIPExportTemplateTable.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportTemplateTable.setDescription('A table of RIP Export template entries.')
basPbrfRIPExportTemplateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1), ).setIndexNames((0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportTemplateChassis"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportTemplateSlot"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportTemplateIf"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportTemplateLPort"), (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportTemplateIndex"))
if mibBuilder.loadTexts: basPbrfRIPExportTemplateEntry.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportTemplateEntry.setDescription('An entry containing management information applicable to an RIP Export PBRF template.')
basPbrfRIPExportTemplateChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 1), BasChassisId())
if mibBuilder.loadTexts: basPbrfRIPExportTemplateChassis.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportTemplateChassis.setDescription('The BAS chassis identifier of this chassis.')
basPbrfRIPExportTemplateSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 2), BasSlotId())
if mibBuilder.loadTexts: basPbrfRIPExportTemplateSlot.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportTemplateSlot.setDescription('The BAS slot ID of this card.')
basPbrfRIPExportTemplateIf = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 3), BasInterfaceId())
if mibBuilder.loadTexts: basPbrfRIPExportTemplateIf.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportTemplateIf.setDescription('The BAS interface ID of this card.')
basPbrfRIPExportTemplateLPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 4), BasLogicalPortId())
if mibBuilder.loadTexts: basPbrfRIPExportTemplateLPort.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportTemplateLPort.setDescription('The BAS logical port ID of this card.')
basPbrfRIPExportTemplateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 5), Integer32())
if mibBuilder.loadTexts: basPbrfRIPExportTemplateIndex.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportTemplateIndex.setDescription('The index of the template')
basPbrfRIPExportTemplateRouteAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 6), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportTemplateRouteAddr.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportTemplateRouteAddr.setDescription('The Route Address key of the template.')
basPbrfRIPExportTemplateRouteMask = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 7), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportTemplateRouteMask.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportTemplateRouteMask.setDescription('The Route Mask key of the template.')
basPbrfRIPExportTemplateIntfAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 8), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportTemplateIntfAddr.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportTemplateIntfAddr.setDescription('The Interface address key of the template.')
basPbrfRIPExportTemplateProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 9), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportTemplateProtocol.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportTemplateProtocol.setDescription('The protocol key of the template.')
basPbrfRIPExportTemplateSpecific = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 10), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportTemplateSpecific.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportTemplateSpecific.setDescription('The specific key of the template.')
basPbrfRIPExportTemplatePeerMask = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 11), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportTemplatePeerMask.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportTemplatePeerMask.setDescription('The peer mask key of the template.')
basPbrfRIPExportTemplateTag = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 12), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportTemplateTag.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportTemplateTag.setDescription('The tag key of the template.')
basPbrfRIPExportTemplateKeyBits = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 13), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportTemplateKeyBits.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportTemplateKeyBits.setDescription('The key bits key mask of the template.')
basPbrfRIPExportTemplateMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 14), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportTemplateMetric.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportTemplateMetric.setDescription('The metric of the template action.')
basPbrfRIPExportTemplateFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 15), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportTemplateFlags.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportTemplateFlags.setDescription('The flags of the template action.')
basPbrfRIPExportTemplateActionTag = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 16), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportTemplateActionTag.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportTemplateActionTag.setDescription('The tag of the template action.')
basPbrfRIPExportTemplateRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 17), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportTemplateRowStatus.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportTemplateRowStatus.setDescription('The row status of the template.')
basPbrfRIPExportTemplateDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 18), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basPbrfRIPExportTemplateDescr.setStatus('current')
if mibBuilder.loadTexts: basPbrfRIPExportTemplateDescr.setDescription('The descr of the RIP Export template.')
mibBuilder.exportSymbols("BAS-PBRF-RIP-MIB", basPbrfRIPImportTemplateIndex=basPbrfRIPImportTemplateIndex, basPbrfRIPImportTemplateRouteMask=basPbrfRIPImportTemplateRouteMask, basPbrfRIPImportFilterTempSlot=basPbrfRIPImportFilterTempSlot, basPbrfRIPExportFilterTempLPort=basPbrfRIPExportFilterTempLPort, basPbrfRIPExportTemplatePeerMask=basPbrfRIPExportTemplatePeerMask, basPbrfRIPExportFilterTempIndex=basPbrfRIPExportFilterTempIndex, basPbrfRIPImportTemplateKeyBits=basPbrfRIPImportTemplateKeyBits, basPbrfRIPImportIndex=basPbrfRIPImportIndex, basPbrfRIPImportTemplateSlot=basPbrfRIPImportTemplateSlot, basPbrfRIPExportFilterTempRowStatus=basPbrfRIPExportFilterTempRowStatus, basPbrfRIPImportChassis=basPbrfRIPImportChassis, basPbrfRIPExportTemplateLPort=basPbrfRIPExportTemplateLPort, basPbrfRIPExportTemplateDescr=basPbrfRIPExportTemplateDescr, basPbrfRIPImportTemplateTag=basPbrfRIPImportTemplateTag, basPbrfRIPMIB=basPbrfRIPMIB, basPbrfRIPImportSlot=basPbrfRIPImportSlot, basPbrfRIPExportFilterTempSlot=basPbrfRIPExportFilterTempSlot, basPbrfRIPImportTemplateChassis=basPbrfRIPImportTemplateChassis, basPbrfRIPExportDescr=basPbrfRIPExportDescr, basPbrfRIPImportTemplatePeerMask=basPbrfRIPImportTemplatePeerMask, basPbrfRIPExportTemplateTable=basPbrfRIPExportTemplateTable, basPbrfRIPExportChassis=basPbrfRIPExportChassis, basPbrfRIPExportTemplateActionTag=basPbrfRIPExportTemplateActionTag, basPbrfRIPImportTemplateIf=basPbrfRIPImportTemplateIf, basPbrfRIPExportTemplateSpecific=basPbrfRIPExportTemplateSpecific, basPbrfRIPImportFilterTempIf=basPbrfRIPImportFilterTempIf, basPbrfRIPImportTemplateCount=basPbrfRIPImportTemplateCount, basPbrfRIPExportTable=basPbrfRIPExportTable, basPbrfRIPExportFilterTempTable=basPbrfRIPExportFilterTempTable, basPbrfRIPImportDescr=basPbrfRIPImportDescr, basPbrfRIPImportTemplateRowStatus=basPbrfRIPImportTemplateRowStatus, basPbrfRIPExportEntry=basPbrfRIPExportEntry, basPbrfRIPExport=basPbrfRIPExport, basPbrfRIPImportTemplateLPort=basPbrfRIPImportTemplateLPort, basPbrfRIPImportTemplateTable=basPbrfRIPImportTemplateTable, basPbrfRIPExportTemplateIntfAddr=basPbrfRIPExportTemplateIntfAddr, basPbrfRIPExportTemplateIndex=basPbrfRIPExportTemplateIndex, basPbrfRIPExportRowStatus=basPbrfRIPExportRowStatus, basPbrfRIPExportFilterTempChassis=basPbrfRIPExportFilterTempChassis, basPbrfRIPImportFilterTempTemplate=basPbrfRIPImportFilterTempTemplate, basPbrfRIPImportFilterTempEntry=basPbrfRIPImportFilterTempEntry, basPbrfRIPExportIf=basPbrfRIPExportIf, basPbrfRIPImportTemplatePref=basPbrfRIPImportTemplatePref, basPbrfRIPExportTemplateFlags=basPbrfRIPExportTemplateFlags, basPbrfRIPExportTemplateEntry=basPbrfRIPExportTemplateEntry, basPbrfRIPExportTemplateRowStatus=basPbrfRIPExportTemplateRowStatus, basPbrfRIPImportTemplateActionTag=basPbrfRIPImportTemplateActionTag, basPbrfRIPExportIndex=basPbrfRIPExportIndex, basPbrfRIPImportRowStatus=basPbrfRIPImportRowStatus, basPbrfRIPImportIf=basPbrfRIPImportIf, basPbrfRIPImportEntry=basPbrfRIPImportEntry, basPbrfRIPImportFilterTempIndex=basPbrfRIPImportFilterTempIndex, basPbrfRIPExportTemplateSlot=basPbrfRIPExportTemplateSlot, basPbrfRIPExportTemplateChassis=basPbrfRIPExportTemplateChassis, basPbrfRIPImportTemplateMetric=basPbrfRIPImportTemplateMetric, basPbrfRIPImportTemplateEntry=basPbrfRIPImportTemplateEntry, basPbrfRIPImportTemplateRouteAddr=basPbrfRIPImportTemplateRouteAddr, basPbrfRIPImportLPort=basPbrfRIPImportLPort, basPbrfRIPExportFilterTempIf=basPbrfRIPExportFilterTempIf, basPbrfRIPExportSlot=basPbrfRIPExportSlot, basPbrfRIPExportFilterTempOrder=basPbrfRIPExportFilterTempOrder, PYSNMP_MODULE_ID=basPbrfRIPMIB, basPbrfRIPExportTemplateRouteAddr=basPbrfRIPExportTemplateRouteAddr, basPbrfRIPImportFilterTempOrder=basPbrfRIPImportFilterTempOrder, basPbrfRIPExportTemplateKeyBits=basPbrfRIPExportTemplateKeyBits, basPbrfRIPImportTable=basPbrfRIPImportTable, basPbrfRIPImportFilterTempTable=basPbrfRIPImportFilterTempTable, basPbrfRIPImportFilterTempChassis=basPbrfRIPImportFilterTempChassis, basPbrfRIPExportTemplateIf=basPbrfRIPExportTemplateIf, basPbrfRIPImport=basPbrfRIPImport, basPbrfRIPImportTemplateFlags=basPbrfRIPImportTemplateFlags, basPbrfRIPExportTemplateRouteMask=basPbrfRIPExportTemplateRouteMask, basPbrfRIPExportTemplateMetric=basPbrfRIPExportTemplateMetric, basPbrfRIPExportFilterTempTemplate=basPbrfRIPExportFilterTempTemplate, basPbrfRIPImportTemplatePeerAddr=basPbrfRIPImportTemplatePeerAddr, basPbrfRIPExportLPort=basPbrfRIPExportLPort, basPbrfRIPImportFilterTempLPort=basPbrfRIPImportFilterTempLPort, basPbrfRIPExportTemplateCount=basPbrfRIPExportTemplateCount, basPbrfRIPImportFilterTempRowStatus=basPbrfRIPImportFilterTempRowStatus, basPbrfRIPExportTemplateProtocol=basPbrfRIPExportTemplateProtocol, basPbrfRIPExportFilterTempEntry=basPbrfRIPExportFilterTempEntry, basPbrfRIPImportTemplateDescr=basPbrfRIPImportTemplateDescr, basPbrfRIPExportTemplateTag=basPbrfRIPExportTemplateTag)
