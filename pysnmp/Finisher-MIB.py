#
# PySNMP MIB module Finisher-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Finisher-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:03:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
hrDeviceIndex, = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "hrDeviceIndex")
PrtMarkerSuppliesTypeTC, PrtMarkerSuppliesClassTC, PrtMediaUnitTC, PrtCapacityUnitTC, prtMIBConformance, PresentOnOff, PrtSubUnitStatusTC, PrtMarkerSuppliesSupplyUnitTC, printmib, PrtInputTypeTC = mibBuilder.importSymbols("Printer-MIB", "PrtMarkerSuppliesTypeTC", "PrtMarkerSuppliesClassTC", "PrtMediaUnitTC", "PrtCapacityUnitTC", "prtMIBConformance", "PresentOnOff", "PrtSubUnitStatusTC", "PrtMarkerSuppliesSupplyUnitTC", "printmib", "PrtInputTypeTC")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, ObjectIdentity, ModuleIdentity, experimental, TimeTicks, Counter32, Gauge32, Unsigned32, IpAddress, MibIdentifier, Integer32, mib_2, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "ModuleIdentity", "experimental", "TimeTicks", "Counter32", "Gauge32", "Unsigned32", "IpAddress", "MibIdentifier", "Integer32", "mib-2", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
finisherMIB = ModuleIdentity((1, 3, 6, 1, 3, 64))
if mibBuilder.loadTexts: finisherMIB.setLastUpdated('9810090000Z')
if mibBuilder.loadTexts: finisherMIB.setOrganization('IETF Printer MIB Working Group')
class FinDeviceTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("stitcher", 3), ("folder", 4), ("binder", 5), ("trimmer", 6), ("dieCutter", 7), ("puncher", 8), ("perforater", 9), ("slitter", 10), ("separationCutter", 11), ("imprinter", 12), ("wrapper", 13), ("bander", 14), ("makeEnvelope", 15), ("stacker", 16), ("sheetRotator", 17))

class FinAttributeTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 31, 40, 50, 80, 81, 82, 83, 100, 130, 160, 161, 162))
    namedValues = NamedValues(("other", 1), ("deviceName", 3), ("deviceVendorName", 4), ("deviceModel", 5), ("deviceVersion", 6), ("deviceSerialNumber", 7), ("maximumSheets", 8), ("finProcessOffsetUnits", 9), ("finReferenceEdge", 10), ("finAxisOffset", 11), ("finJogEdge", 12), ("finHeadLocation", 13), ("finOperationRestrictions", 14), ("finNumberOfPositions", 15), ("namedConfiguration", 16), ("finMediaTypeRestriction", 17), ("finPrinterInputTraySupported", 18), ("finPreviousFinishingOperation", 19), ("finNextFinishingOperation", 20), ("stitchingType", 30), ("stitchingDirection", 31), ("foldingType", 40), ("bindingType", 50), ("punchHoleType", 80), ("punchHoleSizeLongDim", 81), ("punchHoleSizeShortDim", 82), ("punchPattern", 83), ("slittingType", 100), ("wrappingType", 130), ("stackOutputType", 160), ("stackOffset", 161), ("stackRotation", 162))

class FinEdgeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(3, 4, 5, 6))
    namedValues = NamedValues(("topEdge", 3), ("bottomEdge", 4), ("leftEdge", 5), ("rightEdge", 6))

class FinStitchingTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("stapleTopLeft", 4), ("stapleBottomLeft", 5), ("stapleTopRight", 6), ("stapleBottomRight", 7), ("saddleStitch", 8), ("edgeStitch", 9), ("stapleDual", 10))

class StitchingDirTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4))
    namedValues = NamedValues(("unknown", 2), ("topDown", 3), ("bottomUp", 4))

class StitchingAngleTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 2), ("horizontal", 3), ("vertical", 4), ("slanted", 5))

class FinFoldingTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("zFold", 3), ("halfFold", 4), ("letterFold", 5))

class FinBindingTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("tape", 4), ("plastic", 5), ("velo", 6), ("perfect", 7), ("spiral", 8), ("adhesive", 9), ("comb", 10), ("padding", 11))

class FinPunchHoleTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("round", 3), ("oblong", 4), ("square", 5), ("rectangular", 6), ("star", 7))

class FinPunchPatternTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("twoHoleUSTop", 4), ("threeHoleUS", 5), ("twoHoleDIN", 6), ("fourHoleDIN", 7), ("twentyTwoHoleUS", 8), ("nineteenHoleUS", 9), ("twoHoleMetric", 10), ("swedish4Hole", 11), ("twoHoleUSSide", 12), ("fiveHoleUS", 13), ("sevenHoleUS", 14), ("mixed7H4S", 15), ("norweg6Hole", 16), ("metric26Hole", 17), ("metric30Hole", 18))

class FinSlittingTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("slitAndSeparate", 4), ("slitAndMerge", 5))

class FinWrappingTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("shrinkWrap", 4), ("paperWrap", 5))

class FinStackOutputTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("straight", 4), ("offset", 5), ("crissCross", 6))

finDevice = MibIdentifier((1, 3, 6, 1, 2, 1, 43, 30))
finDeviceTable = MibTable((1, 3, 6, 1, 2, 1, 43, 30, 1), )
if mibBuilder.loadTexts: finDeviceTable.setStatus('current')
finDeviceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 43, 30, 1, 1), ).setIndexNames((0, "HOST-RESOURCES-MIB", "hrDeviceIndex"), (0, "Finisher-MIB", "finDeviceIndex"))
if mibBuilder.loadTexts: finDeviceEntry.setStatus('current')
finDeviceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: finDeviceIndex.setStatus('current')
finDeviceType = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 2), FinDeviceTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: finDeviceType.setStatus('current')
finDevicePresentOnOff = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 3), PresentOnOff().clone('notPresent')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finDevicePresentOnOff.setStatus('current')
finDeviceCapacityUnit = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 4), PrtCapacityUnitTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: finDeviceCapacityUnit.setStatus('current')
finDeviceMaxCapacity = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 2147483647)).clone(-2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finDeviceMaxCapacity.setStatus('current')
finDeviceCurrentCapacity = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 2147483647)).clone(-2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finDeviceCurrentCapacity.setStatus('current')
finDeviceAssociatedMediaPaths = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: finDeviceAssociatedMediaPaths.setStatus('current')
finDeviceAssociatedOutputs = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: finDeviceAssociatedOutputs.setStatus('current')
finDeviceStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 9), PrtSubUnitStatusTC().clone(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: finDeviceStatus.setStatus('current')
finDeviceDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: finDeviceDescription.setStatus('current')
finSupply = MibIdentifier((1, 3, 6, 1, 2, 1, 43, 31))
finSupplyTable = MibTable((1, 3, 6, 1, 2, 1, 43, 31, 1), )
if mibBuilder.loadTexts: finSupplyTable.setStatus('current')
finSupplyEntry = MibTableRow((1, 3, 6, 1, 2, 1, 43, 31, 1, 1), ).setIndexNames((0, "HOST-RESOURCES-MIB", "hrDeviceIndex"), (0, "Finisher-MIB", "finSupplyIndex"))
if mibBuilder.loadTexts: finSupplyEntry.setStatus('current')
finSupplyIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: finSupplyIndex.setStatus('current')
finSupplyDeviceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyDeviceIndex.setStatus('current')
finSupplyClass = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 3), PrtMarkerSuppliesClassTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyClass.setStatus('current')
finSupplyType = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 4), PrtMarkerSuppliesTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyType.setStatus('current')
finSupplyDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyDescription.setStatus('current')
finSupplyUnit = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 6), PrtMarkerSuppliesSupplyUnitTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyUnit.setStatus('current')
finSupplyMaxCapacity = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 2147483647)).clone(-2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finSupplyMaxCapacity.setStatus('current')
finSupplyCurrentLevel = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 8), Integer32().clone(-2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finSupplyCurrentLevel.setStatus('current')
finSupplyColorName = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyColorName.setStatus('current')
finSupplyMediaInput = MibIdentifier((1, 3, 6, 1, 2, 1, 43, 32))
finSupplyMediaInputTable = MibTable((1, 3, 6, 1, 2, 1, 43, 32, 1), )
if mibBuilder.loadTexts: finSupplyMediaInputTable.setStatus('current')
finSupplyMediaInputEntry = MibTableRow((1, 3, 6, 1, 2, 1, 43, 32, 1, 1), ).setIndexNames((0, "HOST-RESOURCES-MIB", "hrDeviceIndex"), (0, "Finisher-MIB", "finSupplyMediaInputIndex"))
if mibBuilder.loadTexts: finSupplyMediaInputEntry.setStatus('current')
finSupplyMediaInputIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: finSupplyMediaInputIndex.setStatus('current')
finSupplyMediaInputDeviceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyMediaInputDeviceIndex.setStatus('current')
finSupplyMediaInputSupplyIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyMediaInputSupplyIndex.setStatus('current')
finSupplyMediaInputType = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 4), PrtInputTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyMediaInputType.setStatus('current')
finSupplyMediaInputDimUnit = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 5), PrtMediaUnitTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyMediaInputDimUnit.setStatus('current')
finSupplyMediaInputMediaDimFeedDir = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finSupplyMediaInputMediaDimFeedDir.setStatus('current')
finSupplyMediaInputMediaDimXFeedDir = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finSupplyMediaInputMediaDimXFeedDir.setStatus('current')
finSupplyMediaInputStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 8), PrtSubUnitStatusTC().clone(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyMediaInputStatus.setStatus('current')
finSupplyMediaInputMediaName = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finSupplyMediaInputMediaName.setStatus('current')
finSupplyMediaInputName = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finSupplyMediaInputName.setStatus('current')
finSupplyMediaInputDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyMediaInputDescription.setStatus('current')
finSupplyMediaInputSecurity = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 12), PresentOnOff()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finSupplyMediaInputSecurity.setStatus('current')
finSupplyMediaInputMediaWeight = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finSupplyMediaInputMediaWeight.setStatus('current')
finSupplyMediaInputMediaThickness = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finSupplyMediaInputMediaThickness.setStatus('current')
finSupplyMediaInputMediaType = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finSupplyMediaInputMediaType.setStatus('current')
finDeviceAttribute = MibIdentifier((1, 3, 6, 1, 2, 1, 43, 33))
finDeviceAttributeTable = MibTable((1, 3, 6, 1, 2, 1, 43, 33, 1), )
if mibBuilder.loadTexts: finDeviceAttributeTable.setStatus('current')
finDeviceAttributeEntry = MibTableRow((1, 3, 6, 1, 2, 1, 43, 33, 1, 1), ).setIndexNames((0, "HOST-RESOURCES-MIB", "hrDeviceIndex"), (0, "Finisher-MIB", "finDeviceIndex"), (0, "Finisher-MIB", "finDeviceAttributeTypeIndex"), (0, "Finisher-MIB", "finDeviceAttributeInstanceIndex"))
if mibBuilder.loadTexts: finDeviceAttributeEntry.setStatus('current')
finDeviceAttributeTypeIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 33, 1, 1, 1), FinAttributeTypeTC())
if mibBuilder.loadTexts: finDeviceAttributeTypeIndex.setStatus('current')
finDeviceAttributeInstanceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 33, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: finDeviceAttributeInstanceIndex.setStatus('current')
finDeviceAttributeValueAsInteger = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 33, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 2147483647)).clone(-2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finDeviceAttributeValueAsInteger.setStatus('current')
finDeviceAttributeValueAsOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 33, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finDeviceAttributeValueAsOctets.setStatus('current')
finMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 43, 2, 3)).setObjects(("Finisher-MIB", "finDeviceGroup"), ("Finisher-MIB", "finSupplyGroup"), ("Finisher-MIB", "finDeviceAttributeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    finMIBCompliance = finMIBCompliance.setStatus('current')
finMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 43, 2, 4))
finDeviceGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 43, 2, 4, 1)).setObjects(("Finisher-MIB", "finDeviceType"), ("Finisher-MIB", "finDevicePresentOnOff"), ("Finisher-MIB", "finDeviceCapacityUnit"), ("Finisher-MIB", "finDeviceMaxCapacity"), ("Finisher-MIB", "finDeviceCurrentCapacity"), ("Finisher-MIB", "finDeviceAssociatedMediaPaths"), ("Finisher-MIB", "finDeviceAssociatedOutputs"), ("Finisher-MIB", "finDeviceStatus"), ("Finisher-MIB", "finDeviceDescription"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    finDeviceGroup = finDeviceGroup.setStatus('current')
finSupplyGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 43, 2, 4, 2)).setObjects(("Finisher-MIB", "finSupplyDeviceIndex"), ("Finisher-MIB", "finSupplyClass"), ("Finisher-MIB", "finSupplyType"), ("Finisher-MIB", "finSupplyDescription"), ("Finisher-MIB", "finSupplyUnit"), ("Finisher-MIB", "finSupplyMaxCapacity"), ("Finisher-MIB", "finSupplyCurrentLevel"), ("Finisher-MIB", "finSupplyColorName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    finSupplyGroup = finSupplyGroup.setStatus('current')
finSupplyMediaInputGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 43, 2, 4, 3)).setObjects(("Finisher-MIB", "finSupplyMediaInputDeviceIndex"), ("Finisher-MIB", "finSupplyMediaInputSupplyIndex"), ("Finisher-MIB", "finSupplyMediaInputType"), ("Finisher-MIB", "finSupplyMediaInputDimUnit"), ("Finisher-MIB", "finSupplyMediaInputMediaDimFeedDir"), ("Finisher-MIB", "finSupplyMediaInputMediaDimXFeedDir"), ("Finisher-MIB", "finSupplyMediaInputStatus"), ("Finisher-MIB", "finSupplyMediaInputMediaName"), ("Finisher-MIB", "finSupplyMediaInputName"), ("Finisher-MIB", "finSupplyMediaInputDescription"), ("Finisher-MIB", "finSupplyMediaInputSecurity"), ("Finisher-MIB", "finSupplyMediaInputMediaWeight"), ("Finisher-MIB", "finSupplyMediaInputMediaThickness"), ("Finisher-MIB", "finSupplyMediaInputMediaType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    finSupplyMediaInputGroup = finSupplyMediaInputGroup.setStatus('current')
finDeviceAttributeGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 43, 2, 4, 4)).setObjects(("Finisher-MIB", "finDeviceAttributeValueAsInteger"), ("Finisher-MIB", "finDeviceAttributeValueAsOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    finDeviceAttributeGroup = finDeviceAttributeGroup.setStatus('current')
mibBuilder.exportSymbols("Finisher-MIB", PYSNMP_MODULE_ID=finisherMIB, finSupplyMediaInputMediaType=finSupplyMediaInputMediaType, finSupplyMediaInputName=finSupplyMediaInputName, finDeviceAttributeTypeIndex=finDeviceAttributeTypeIndex, finSupplyGroup=finSupplyGroup, finDeviceTable=finDeviceTable, finSupplyDeviceIndex=finSupplyDeviceIndex, finDeviceType=finDeviceType, finSupplyMediaInput=finSupplyMediaInput, finSupplyMediaInputMediaDimFeedDir=finSupplyMediaInputMediaDimFeedDir, FinStackOutputTypeTC=FinStackOutputTypeTC, FinEdgeTC=FinEdgeTC, finSupplyMediaInputMediaDimXFeedDir=finSupplyMediaInputMediaDimXFeedDir, finSupplyMediaInputMediaName=finSupplyMediaInputMediaName, finDeviceAttributeValueAsOctets=finDeviceAttributeValueAsOctets, finSupplyEntry=finSupplyEntry, finDeviceStatus=finDeviceStatus, finDeviceAttributeValueAsInteger=finDeviceAttributeValueAsInteger, FinDeviceTypeTC=FinDeviceTypeTC, FinFoldingTypeTC=FinFoldingTypeTC, finDeviceAssociatedOutputs=finDeviceAssociatedOutputs, FinPunchPatternTC=FinPunchPatternTC, finSupplyCurrentLevel=finSupplyCurrentLevel, finSupplyMediaInputTable=finSupplyMediaInputTable, finSupplyMediaInputMediaThickness=finSupplyMediaInputMediaThickness, finDeviceMaxCapacity=finDeviceMaxCapacity, finDeviceAttributeTable=finDeviceAttributeTable, finDeviceGroup=finDeviceGroup, finSupplyMediaInputDimUnit=finSupplyMediaInputDimUnit, finSupplyMediaInputIndex=finSupplyMediaInputIndex, finSupplyMediaInputEntry=finSupplyMediaInputEntry, finSupplyMediaInputSecurity=finSupplyMediaInputSecurity, FinBindingTypeTC=FinBindingTypeTC, StitchingDirTypeTC=StitchingDirTypeTC, finDeviceCurrentCapacity=finDeviceCurrentCapacity, finDeviceAssociatedMediaPaths=finDeviceAssociatedMediaPaths, finSupplyIndex=finSupplyIndex, finSupplyType=finSupplyType, finSupplyMaxCapacity=finSupplyMaxCapacity, FinStitchingTypeTC=FinStitchingTypeTC, finDeviceDescription=finDeviceDescription, finSupplyMediaInputDeviceIndex=finSupplyMediaInputDeviceIndex, FinPunchHoleTypeTC=FinPunchHoleTypeTC, finisherMIB=finisherMIB, finSupplyColorName=finSupplyColorName, finMIBGroups=finMIBGroups, finSupplyMediaInputGroup=finSupplyMediaInputGroup, finSupplyMediaInputType=finSupplyMediaInputType, finDeviceAttributeGroup=finDeviceAttributeGroup, finSupplyMediaInputSupplyIndex=finSupplyMediaInputSupplyIndex, finSupplyClass=finSupplyClass, FinWrappingTypeTC=FinWrappingTypeTC, finMIBCompliance=finMIBCompliance, finSupplyTable=finSupplyTable, finDeviceEntry=finDeviceEntry, finDevicePresentOnOff=finDevicePresentOnOff, finSupplyMediaInputDescription=finSupplyMediaInputDescription, finDeviceCapacityUnit=finDeviceCapacityUnit, finSupplyUnit=finSupplyUnit, finSupplyMediaInputStatus=finSupplyMediaInputStatus, finDeviceAttribute=finDeviceAttribute, finDevice=finDevice, FinAttributeTypeTC=FinAttributeTypeTC, StitchingAngleTypeTC=StitchingAngleTypeTC, finSupply=finSupply, finSupplyDescription=finSupplyDescription, finSupplyMediaInputMediaWeight=finSupplyMediaInputMediaWeight, finDeviceAttributeEntry=finDeviceAttributeEntry, FinSlittingTypeTC=FinSlittingTypeTC, finDeviceIndex=finDeviceIndex, finDeviceAttributeInstanceIndex=finDeviceAttributeInstanceIndex)
