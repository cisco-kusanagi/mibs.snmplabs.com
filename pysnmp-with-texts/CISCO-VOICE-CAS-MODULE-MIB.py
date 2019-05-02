#
# PySNMP MIB module CISCO-VOICE-CAS-MODULE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VOICE-CAS-MODULE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:18:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
EntPhysicalIndexOrZero, = mibBuilder.importSymbols("CISCO-TC", "EntPhysicalIndexOrZero")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter64, Counter32, IpAddress, Unsigned32, MibIdentifier, NotificationType, Integer32, TimeTicks, Bits, iso, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter64", "Counter32", "IpAddress", "Unsigned32", "MibIdentifier", "NotificationType", "Integer32", "TimeTicks", "Bits", "iso", "ModuleIdentity", "ObjectIdentity")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoVoiceCasModuleMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 389))
ciscoVoiceCasModuleMIB.setRevisions(('2004-03-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVoiceCasModuleMIB.setRevisionsDescriptions(('Initial version of the MIB',))
if mibBuilder.loadTexts: ciscoVoiceCasModuleMIB.setLastUpdated('200403150000Z')
if mibBuilder.loadTexts: ciscoVoiceCasModuleMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVoiceCasModuleMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-voice-gateway@cisco.com')
if mibBuilder.loadTexts: ciscoVoiceCasModuleMIB.setDescription('This MIB is used to support Programmable CAS signaling Bit configuration on modules that support voice traffic. This MIB will enable programming of the CAS bits in order to translate incoming/outgoing bit patterns from/to the TDM or packet side interface. Terminology: ABCD - Signaling bits describing off-hook, on-hook, idle, flash, etc events. DSP - Digital Signal Processing CAS - Channal Associated Signaling E&M - Ear and Mouth Protocol TDM - Time Division Multiplexed ')
ciscoVoiceCasModuleNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 389, 0))
ciscoVoiceCasModuleObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 389, 1))
cvcmCasConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1))
class CvcmCasPatternBitPosition(TextualConvention, Bits):
    description = 'Defines the bit positions for the incoming and outgoing ABCD bit patterns. All positions need to be set to 0 or 1 in order to have the correct pattern. dBit : Position of the D bit in the ABCD bit pattern cBit : Position of the C bit in the ABCD bit pattern bBit : Position of the B bit in the ABCD bit pattern aBit : Position of the A bit in the ABCD bit pattern '
    status = 'current'
    namedValues = NamedValues(("dBit", 0), ("cBit", 1), ("bBit", 2), ("aBit", 3))

class CvcmCasBitAction(TextualConvention, Integer32):
    description = 'Defines the actions that can be performed on the CAS ABCD bits. casBitNoAction : No action on the bit specifed. Maintain incoming bit value. casBitSetToZero : Set bit to zero casBitSetToOne : Set bit to one casBitInvertBit : Invert incoming bit casBitInvertABit : Invert A bit and apply to the bit location specified casBitInvertBBit : Invert B bit and apply to the bit location specified casBitInvertCBit : Invert C bit and apply to the bit location specified casBitInvertDBit : Invert D bit and apply to the bit location specified casBitABit : Apply A bit value to the bit location specified casBitBBit : Apply B bit value to the bit location specified casBitCBit : Apply C bit value to the bit location specified casBitDBit : Apply D bit value to the bit location specified '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("casBitNoAction", 1), ("casBitSetToZero", 2), ("casBitSetToOne", 3), ("casBitInvertBit", 4), ("casBitInvertABit", 5), ("casBitInvertBBit", 6), ("casBitInvertCBit", 7), ("casBitInvertDBit", 8), ("casBitABit", 9), ("casBitBBit", 10), ("casBitCBit", 11), ("casBitDBit", 12))

cvcmABCDBitTemplateConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1), )
if mibBuilder.loadTexts: cvcmABCDBitTemplateConfigTable.setStatus('current')
if mibBuilder.loadTexts: cvcmABCDBitTemplateConfigTable.setDescription("This table is used to configure templates on the module/card. These templates provide mapping information between the incoming CAS ABCD signaling bit patterns and the outgoing ABCD signaling bit patterns. The outgoing bit patterns are derived from the incoming bit patterns by applying a set of actions to each incoming bit. Thus, this table essentially contains configuration information about CAS ABCD signaling bits. The ABCD bit carries signaling information describing off-hook, on-hook event etc on a T1 or E1. The pattern representations differ in CAS variants on a T1 and E1. For example: On T1: E&M protocol ABCD seized is 1100 On E1: CAS-R2 signaling ABCD seized is 0001 This table is configured on a per module/ card basis. Further, one can have multiple different actions performed on the different bits (A, B, C or D) consecutively for the same incoming ABCD bit index. However, a given bit position can only have one action being performed on it for a given incoming bit pattern. For example, for a given incoming bit index, one can define the 'A' bit to be set to 0, the 'B' bit to be swapped with the 'C' bit, the 'C' bit to be swapped with the 'B' bit and the 'D' bit to be inverted. Thus, using this table, the user can create a template with name (cvcmCasTemplateName) 'Template1' where for incoming pattern (cvcmABCDIncomingPattern) '0000', the action on the A bit (cvcmCasABitAction) is 'casBitSetToZero', the action on the B bit (cvcmCasBBitAction) is 'casBitCBit', the action on the C bit (cvcmCasCBitAction) is 'casBitBBit' and the action on the D bit (cvcmCasDBitAction) is 'casBitInvertBit'. This will create one entry in 'Template1' where the resultant outgoing pattern (cvcmABCDOutgoingPattern) will be '0001'. ")
cvcmABCDBitTemplateConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-VOICE-CAS-MODULE-MIB", "cvcmModuleIndex"), (0, "CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasTemplateIndex"), (0, "CISCO-VOICE-CAS-MODULE-MIB", "cvcmABCDPatternIndex"))
if mibBuilder.loadTexts: cvcmABCDBitTemplateConfigEntry.setStatus('current')
if mibBuilder.loadTexts: cvcmABCDBitTemplateConfigEntry.setDescription('An entry in the table. Each entry consists of user defined CAS ABCD bit information to configure a transmit or received signaling channel on a DSP. ')
cvcmModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: cvcmModuleIndex.setStatus('current')
if mibBuilder.loadTexts: cvcmModuleIndex.setDescription(" This object uniquely identifies the card/ module where this table resides. It could be the slot number of the module or be 1 where 'module' is not applicable. ")
cvcmCasTemplateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: cvcmCasTemplateIndex.setStatus('current')
if mibBuilder.loadTexts: cvcmCasTemplateIndex.setDescription('This object will index into the template that is configured in this table. ')
cvcmABCDPatternIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: cvcmABCDPatternIndex.setStatus('current')
if mibBuilder.loadTexts: cvcmABCDPatternIndex.setDescription('Will be used to index into a particular pattern mapping in the template that is configured. Since there are only 4 signaling bits (A, B, C, D), there can only be (2^4) or 16 patterns per template. ')
cvcmModulePhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 4), EntPhysicalIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcmModulePhysicalIndex.setStatus('current')
if mibBuilder.loadTexts: cvcmModulePhysicalIndex.setDescription('This object represents the entPhysicalIndex of the module where this table is being configured. If the entPhysicalTable is not supported on the SNMP agent, then the value of this object will be zero. ')
cvcmCasTemplateName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 5), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcmCasTemplateName.setStatus('current')
if mibBuilder.loadTexts: cvcmCasTemplateName.setDescription('This object identifies the name of the template configured. This object needs to be unique among all the instances of the cvcmABCDBitTemplateConfigTable. The SNMP agent will need to validate this value for uniqueness. ')
cvcmABCDIncomingPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 6), CvcmCasPatternBitPosition()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcmABCDIncomingPattern.setStatus('current')
if mibBuilder.loadTexts: cvcmABCDIncomingPattern.setDescription("This object identifies the ABCD signaling bits that are received by the module. The actions specified in 'cvcmCasABitAction', 'cvcmCasBBitAction', 'cvcmCasCBitAction' and 'cvcmCasDBitAction' are applied to this object. ")
cvcmABCDOutgoingPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 7), CvcmCasPatternBitPosition()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcmABCDOutgoingPattern.setStatus('current')
if mibBuilder.loadTexts: cvcmABCDOutgoingPattern.setDescription("This object identifies the ABCD signaling bits defined by user, and downloaded to DSP signaling channel. This pattern is derived from the actions specified in 'cvcmCasABitAction', 'cvcmCasBBitAction', 'cvcmCasCBitAction' and 'cvcmCasDBitAction'. The same pattern can map to different cvcmABCDIncomingPattern depending on the set of actions. This pattern is mapped to input ABCD bit pattern received and reported to the TDM or network side. ")
cvcmCasABitAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 8), CvcmCasBitAction().clone('casBitABit')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcmCasABitAction.setStatus('current')
if mibBuilder.loadTexts: cvcmCasABitAction.setDescription("This object identifies the action on the 'A' bit of the incoming ABCD bit pattern specified in cvcmABCDIncomingPattern. For this object, 'cvcmInvertBit' is same as 'cvcmInvertABit', 'cvcmNoAction' is same as 'cvcmABit'. ")
cvcmCasBBitAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 9), CvcmCasBitAction().clone('casBitBBit')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcmCasBBitAction.setStatus('current')
if mibBuilder.loadTexts: cvcmCasBBitAction.setDescription("This object identifies the action on the 'B' bit of the incoming ABCD bit pattern specified in cvcmABCDIncomingPattern. For this object, 'cvcmInvertBit' is same as 'cvcmInvertBBit', 'cvcmNoAction' is same as 'cvcmBBit'. ")
cvcmCasCBitAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 10), CvcmCasBitAction().clone('casBitCBit')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcmCasCBitAction.setStatus('current')
if mibBuilder.loadTexts: cvcmCasCBitAction.setDescription("This object identifies the action on the 'C' bit of the incoming ABCD bit pattern specified in cvcmABCDIncomingPattern. For this object, 'cvcmInvertBit' is same as 'cvcmInvertCBit', 'cvcmNoAction' is same as 'cvcmCBit'. ")
cvcmCasDBitAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 11), CvcmCasBitAction().clone('casBitDBit')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcmCasDBitAction.setStatus('current')
if mibBuilder.loadTexts: cvcmCasDBitAction.setDescription("This object identifies the action on the 'D' bit of the incoming ABCD bit pattern specified in cvcmABCDIncomingPattern. For this object, 'cvcmInvertBit' is same as 'cvcmInvertDBit', 'cvcmNoAction' is same as 'cvcmDBit'. ")
cvcmCasBitRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcmCasBitRowStatus.setStatus('current')
if mibBuilder.loadTexts: cvcmCasBitRowStatus.setDescription("An entry may be created using the 'createAndGo' option. When the row is successfully created, the object will be set to 'active' by the agent. An entry may be deleted by setting the object to 'destroy'. ")
cvcmMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 389, 2))
cvcmMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 389, 2, 1))
cvcmMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 389, 2, 2))
ciscoVoiceCasModuleMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 389, 2, 2, 1)).setObjects(("CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasBitGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceCasModuleMIBCompliance = ciscoVoiceCasModuleMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoVoiceCasModuleMIBCompliance.setDescription('Compliance statement for CISCO-VOICE-CAS-MODULE-MIB.')
cvcmCasBitGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 389, 2, 1, 1)).setObjects(("CISCO-VOICE-CAS-MODULE-MIB", "cvcmModulePhysicalIndex"), ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasTemplateName"), ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmABCDIncomingPattern"), ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmABCDOutgoingPattern"), ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasABitAction"), ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasBBitAction"), ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasCBitAction"), ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasDBitAction"), ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasBitRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcmCasBitGroup = cvcmCasBitGroup.setStatus('current')
if mibBuilder.loadTexts: cvcmCasBitGroup.setDescription('A collection of objects used for configuring DSP signaling channel. ')
mibBuilder.exportSymbols("CISCO-VOICE-CAS-MODULE-MIB", cvcmCasDBitAction=cvcmCasDBitAction, cvcmABCDBitTemplateConfigTable=cvcmABCDBitTemplateConfigTable, cvcmCasTemplateIndex=cvcmCasTemplateIndex, cvcmModulePhysicalIndex=cvcmModulePhysicalIndex, PYSNMP_MODULE_ID=ciscoVoiceCasModuleMIB, cvcmABCDIncomingPattern=cvcmABCDIncomingPattern, cvcmMIBCompliances=cvcmMIBCompliances, ciscoVoiceCasModuleObjects=ciscoVoiceCasModuleObjects, cvcmCasBBitAction=cvcmCasBBitAction, cvcmMIBConformance=cvcmMIBConformance, CvcmCasBitAction=CvcmCasBitAction, cvcmMIBGroups=cvcmMIBGroups, cvcmCasTemplateName=cvcmCasTemplateName, ciscoVoiceCasModuleMIBCompliance=ciscoVoiceCasModuleMIBCompliance, cvcmABCDBitTemplateConfigEntry=cvcmABCDBitTemplateConfigEntry, cvcmModuleIndex=cvcmModuleIndex, cvcmCasConfig=cvcmCasConfig, cvcmABCDPatternIndex=cvcmABCDPatternIndex, cvcmCasBitRowStatus=cvcmCasBitRowStatus, ciscoVoiceCasModuleNotifs=ciscoVoiceCasModuleNotifs, cvcmCasABitAction=cvcmCasABitAction, cvcmABCDOutgoingPattern=cvcmABCDOutgoingPattern, cvcmCasCBitAction=cvcmCasCBitAction, cvcmCasBitGroup=cvcmCasBitGroup, ciscoVoiceCasModuleMIB=ciscoVoiceCasModuleMIB, CvcmCasPatternBitPosition=CvcmCasPatternBitPosition)
