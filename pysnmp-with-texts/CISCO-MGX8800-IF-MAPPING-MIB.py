#
# PySNMP MIB module CISCO-MGX8800-IF-MAPPING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MGX8800-IF-MAPPING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:07:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, NotificationType, ObjectIdentity, Counter64, Integer32, IpAddress, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "NotificationType", "ObjectIdentity", "Counter64", "Integer32", "IpAddress", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoMGX8800IfMappingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 7))
ciscoMGX8800IfMappingMIB.setRevisions(('2004-05-25 00:00', '2004-04-30 00:00', '2003-12-04 00:00', '2003-03-20 00:00', '2002-10-21 00:00', '2002-10-16 00:00', '2002-05-21 00:00', '2002-02-17 00:00', '2001-10-16 00:00', '2001-07-08 00:00', '2000-02-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMGX8800IfMappingMIB.setRevisionsDescriptions(('Added following enums to CmimIfType: lapd(24). ', 'Added following enums to CmimIfType: ppplink(22), pppMultilinkBundle(23), ', 'Added new enum mfrBundle(21) to CmimIfType. ', 'Fixed alignments and descriptions. ', '1. Added following enums to CmimIfType: ds1VTPath(18), ds1Ds3SonetPath(19) and atmVciEndPt(20) 2. Modified description for cmimModuleIndex, CmimIfType and cmimIfNumber to describe the rules to form a query to obtain ifIndex for ds1VTPath, ds1Ds3SonetPath and atmVciEndPt. ', '1. Added following enums to CmimIfType: frameRelayPort(16), ces(17). 2. Modified description for cmimModuleIndex, CmimIfType and cmimIfNumber to describe the rules to form a query to obtain ifIndex for frame relay and ces interfaces. ', '1. Added following enums to CmimIfType: sonetPath(12), ds3SonetPath(13), atmSonetPath(14), atmDs3SonetPath(15). 2. Modified description for cmimModuleIndex, CmimIfType and cmimIfNumber to describe the rules to form a query to obtain ifIndex for SONET Path, ds3 path on a SONET path and corresponding ATM Cell layers. 3. Imported Unsigned32 from SNMPv2-SMI instead of CISCO-TC. ', 'Added enums srmBertLine(10) and srmBertPort(11) to CmimIfType and modified descriptions of cmimIfNumber and CmimIfType, explaining how to discover the interface indexes of physical lines and logical ports of narrow-band service modules (NBSM) that obtain BERT service through Service Resource Module (SRM). ', 'Added enum sonetVT(8) and imaGrpAtmPhy(9) for CmimIfType, and modified descriptions for cmimIfNumber and CmimIfType. ', 'Added following enumerations to Textual-convention CmimIfType: adjCardApsLine(6), propAtm(7). ', 'Initial version of this MIB Module',))
if mibBuilder.loadTexts: ciscoMGX8800IfMappingMIB.setLastUpdated('200405250000Z')
if mibBuilder.loadTexts: ciscoMGX8800IfMappingMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMGX8800IfMappingMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoMGX8800IfMappingMIB.setDescription('This MIB module is used for getting the ifIndex values given physical location and/or logical information. The physical information includes the slot, back-card and physical line, IMA group ID, MFR (Multilink Frame Relay) bundle etc. The logical information includes the logical interface or virtual interface number. In this MIB back card, bay, line module are used to refer to the back card. ')
class CmimIfType(TextualConvention, Integer32):
    description = 'The interface types. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))
    namedValues = NamedValues(("physicalLine", 1), ("atmIma", 2), ("atm", 3), ("atmVirtual", 4), ("ds1Inds3", 5), ("adjCardApsLine", 6), ("propAtm", 7), ("sonetVT", 8), ("imaGrpAtmPhy", 9), ("srmBertLine", 10), ("srmBertPort", 11), ("sonetPath", 12), ("ds3SonetPath", 13), ("atmSonetPath", 14), ("atmDs3SonetPath", 15), ("frameRelayPort", 16), ("ces", 17), ("ds1VTPath", 18), ("ds1Ds3SonetPath", 19), ("atmVciEndPt", 20), ("mfrBundle", 21), ("ppplink", 22), ("pppMpbundle", 23), ("lapd", 24))

cmimMappingObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 7, 1))
cmimPhysToIf = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 7, 1, 1))
cmimPhysToIfTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 7, 1, 1, 1), )
if mibBuilder.loadTexts: cmimPhysToIfTable.setStatus('current')
if mibBuilder.loadTexts: cmimPhysToIfTable.setDescription('This table contains one or more rows, representing mappings of physical or logical interfaces to ifIndex values. ')
cmimPhysToIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 7, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-MGX8800-IF-MAPPING-MIB", "cmimModuleIndex"), (0, "CISCO-MGX8800-IF-MAPPING-MIB", "cmimIfNumber"), (0, "CISCO-MGX8800-IF-MAPPING-MIB", "cmimIfType"))
if mibBuilder.loadTexts: cmimPhysToIfEntry.setStatus('current')
if mibBuilder.loadTexts: cmimPhysToIfEntry.setDescription('Information about a particular physical interface or logical interface. ')
cmimModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 7, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cmimModuleIndex.setStatus('current')
if mibBuilder.loadTexts: cmimModuleIndex.setDescription('An index value that uniquely identifies the location of the module or a physical line. It has the information on slot number, back card and physical line number. Following is the mapping used for this object. Mapping used when cmimIfType is physicalLine(1), atm(3), adjCardApsLine(6), imaGrpAtmPhy(9) and mfrBundle(21) Bits 0-7 : Ignored Bits 8-15 : Back Card Number (0 - Ignored, 1-Top Back card 2 - Bottom Back card) Bits 16-23 : Logical slot number Bits 24-31 : Shelf number (1 - Currently, only value 1 is supported) Mapping used when cmimIfType is set to ds1Inds3(5), sonetVT(8), sonetPath(12), ds3SonetPath(13), atmSonetPath(14), atmDs3SonetPath(15), ds1VTPath(18), ds1Ds3SonetPath(19) and lapd(24) Bits 0-7 : DS3/E3/Sonet/Sdh physical line number Bits 8-15 : Back Card Number (0 - Ignored, 1-Top Back card 2 - Bottom Back card. Bits 16-23 : Logical slot number Bits 24-31 : Shelf number (1 - Currently, only value 1 is supported) Mapping used when cmimIfType is set to propAtm(7), frameRelayPort(16), ces(17), atmVciEndPt(20), ppplink(22) and pppMpbundle(23). Bits 0-7 : 0 Ignored Bits 8-15 : 0 Ignored Bits 16-23 : Logical slot number Bits 24-31 : Shelf number (1 - only value 1 is supported) Mapping used when cmimIfType is set to srmBertLine(10) or srmBertPort(11) Bits 0-7 : 0 Ignored Bits 8-15 : Logical slot number of NBSM Bits 16-23 : Logical slot number of SRM Bits 24-31 : Shelf number (1 - only value 1 is supported) ')
cmimIfNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 7, 1, 1, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: cmimIfNumber.setStatus('current')
if mibBuilder.loadTexts: cmimIfNumber.setDescription('An index value uniquely identifies the interface number (physical, logical) of the module. The value specified depends on the value specified in cmimIfType. cmimIfType cmimIfNumber ---------- ------------ physicalLine(1) physical line number atm(3) physical line number for atm phy number ds1Inds3(5) DS1/E1 line number in a DS3/E3 adjCardApsLine(6) adjacent card APS line number propAtm(7) set to 1, this is the only value supported at this time sonetVT(8) DSxN tributary in a sonet/sdh line imaGrpAtmPhy(9) atm ima group for atm phy number srmBertLine(10) physical line number of NBSM srmBertPort(11) logical port number of NBSM. sonetPath(12) STS-1/AU-3 Path Number atmSonetPath(14) STS-1/AU-3 Path Number ds3SonetPath(13) Bits 0..15 : STS-1/AU-3 Path Number Bits 16..31: 1 for STS-1/AU-3 or DS3 Number within AU-4 atmDs3SonetPath(15) Bits 0..15 : STS-1/AU-3 Path Number Bits 16..31: 1 for STS-1/AU-3 or DS3 Number within AU-4 frameRelayPort(16) logical port number for frame interface ces(17) logical port number of circuit emulation service interface ds1InVT(18) Bits 0..7 : VT Number Bits 8..15: VT group number Bits 16..31: STS-1/AU-3 Path Number ds1Ds3SonetPath(19) Bits 0..7 : ds1 Number Bits 8..15: ds3 Number Bits 16..31: STS Path Number atmVciEndPt(20) Bits 0..15 : VCI Bits 16..27: VPI Bits 28..31: Port(ATM) mfrBundle(21) Multilink Frame Relay bundle number ppplink(22) ppp index of the ppp interface pppMpbundle(23) mpbundle index of the mpbundle interface lapd(24) Bits 0..7 : ds0 number Bits 8..15 : VT number or ds1 number Bits 16..23: VT group (DS3 ignore it) Bits 24..31: STS or DS3 path ')
cmimIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 7, 1, 1, 1, 1, 3), CmimIfType())
if mibBuilder.loadTexts: cmimIfType.setStatus('current')
if mibBuilder.loadTexts: cmimIfType.setDescription('The type of interface specified by cmimIfNumber.')
cmimIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 7, 1, 1, 1, 1, 4), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmimIfIndex.setStatus('current')
if mibBuilder.loadTexts: cmimIfIndex.setDescription('The value of the instance of the ifIndex object, defined in MIB-II, for the interface corresponding to the INDEXes specified in the table. Note that the values returned for cmimIfType=srmBertLine(10) and cmimIfType=srmBertPort(11) will not have any entries in the IF-TABLE. ')
cmimPhysToIfMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 7, 3))
cmimPhysToIfMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 7, 3, 1))
cmimPhysToIfMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 7, 3, 2))
cmimPhysToIfMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 7, 3, 1, 1)).setObjects(("CISCO-MGX8800-IF-MAPPING-MIB", "cmimPhysToIfMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmimPhysToIfMIBCompliance = cmimPhysToIfMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cmimPhysToIfMIBCompliance.setDescription('The compliance statement for cmimPhystoIfTable. ')
cmimPhysToIfMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 7, 3, 2, 1)).setObjects(("CISCO-MGX8800-IF-MAPPING-MIB", "cmimIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmimPhysToIfMIBGroup = cmimPhysToIfMIBGroup.setStatus('current')
if mibBuilder.loadTexts: cmimPhysToIfMIBGroup.setDescription('This group has to be implemented on all MGX8800 series products. ')
mibBuilder.exportSymbols("CISCO-MGX8800-IF-MAPPING-MIB", cmimPhysToIfMIBGroups=cmimPhysToIfMIBGroups, cmimIfIndex=cmimIfIndex, cmimPhysToIfMIBCompliance=cmimPhysToIfMIBCompliance, ciscoMGX8800IfMappingMIB=ciscoMGX8800IfMappingMIB, CmimIfType=CmimIfType, cmimMappingObjects=cmimMappingObjects, cmimPhysToIf=cmimPhysToIf, PYSNMP_MODULE_ID=ciscoMGX8800IfMappingMIB, cmimPhysToIfEntry=cmimPhysToIfEntry, cmimPhysToIfMIBCompliances=cmimPhysToIfMIBCompliances, cmimPhysToIfTable=cmimPhysToIfTable, cmimPhysToIfMIBConformance=cmimPhysToIfMIBConformance, cmimModuleIndex=cmimModuleIndex, cmimPhysToIfMIBGroup=cmimPhysToIfMIBGroup, cmimIfNumber=cmimIfNumber, cmimIfType=cmimIfType)
