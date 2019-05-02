#
# PySNMP MIB module Finisher-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Finisher-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:16:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
hrDeviceIndex, = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "hrDeviceIndex")
printmib, PrtMediaUnitTC, PresentOnOff, PrtInputTypeTC, PrtCapacityUnitTC, PrtMarkerSuppliesTypeTC, PrtMarkerSuppliesSupplyUnitTC, PrtSubUnitStatusTC, PrtMarkerSuppliesClassTC, prtMIBConformance = mibBuilder.importSymbols("Printer-MIB", "printmib", "PrtMediaUnitTC", "PresentOnOff", "PrtInputTypeTC", "PrtCapacityUnitTC", "PrtMarkerSuppliesTypeTC", "PrtMarkerSuppliesSupplyUnitTC", "PrtSubUnitStatusTC", "PrtMarkerSuppliesClassTC", "prtMIBConformance")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Gauge32, mib_2, iso, experimental, TimeTicks, ModuleIdentity, Integer32, Counter32, Counter64, Unsigned32, NotificationType, IpAddress, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "mib-2", "iso", "experimental", "TimeTicks", "ModuleIdentity", "Integer32", "Counter32", "Counter64", "Unsigned32", "NotificationType", "IpAddress", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
finisherMIB = ModuleIdentity((1, 3, 6, 1, 3, 64))
if mibBuilder.loadTexts: finisherMIB.setLastUpdated('9810090000Z')
if mibBuilder.loadTexts: finisherMIB.setOrganization('IETF Printer MIB Working Group')
if mibBuilder.loadTexts: finisherMIB.setContactInfo("Ron Bergman Dataproducts Corp. 1757 Tapo Canyon Road Simi Valley, CA 91063-3394 rbergma@dpc.com Send comments to the printmib WG using the Finisher MIB Project (FIN) Mailing List: fin@pwg.org For further information, access the PWG web page under 'FIN': http://www.pwg.org/ Implementers of this specification are encouraged to join the fin mailing list in order to participate in discussions on any clarifications needed and registration proposals being reviewed in order to achieve consensus.")
if mibBuilder.loadTexts: finisherMIB.setDescription('The MIB module for management of printer finisher units. The Finisher MIB is an extension of the Printer MIB.')
class FinDeviceTypeTC(TextualConvention, Integer32):
    description = 'The defined finishing device subunit process enumerations.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("stitcher", 3), ("folder", 4), ("binder", 5), ("trimmer", 6), ("dieCutter", 7), ("puncher", 8), ("perforater", 9), ("slitter", 10), ("separationCutter", 11), ("imprinter", 12), ("wrapper", 13), ("bander", 14), ("makeEnvelope", 15), ("stacker", 16), ("sheetRotator", 17))

class FinAttributeTypeTC(TextualConvention, Integer32):
    description = 'This textual convention defines the set of enums for use in the finDeviceAttributeTable. See section 5.7 for the complete specification of each attribute.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 31, 40, 50, 80, 81, 82, 83, 100, 130, 160, 161, 162))
    namedValues = NamedValues(("other", 1), ("deviceName", 3), ("deviceVendorName", 4), ("deviceModel", 5), ("deviceVersion", 6), ("deviceSerialNumber", 7), ("maximumSheets", 8), ("finProcessOffsetUnits", 9), ("finReferenceEdge", 10), ("finAxisOffset", 11), ("finJogEdge", 12), ("finHeadLocation", 13), ("finOperationRestrictions", 14), ("finNumberOfPositions", 15), ("namedConfiguration", 16), ("finMediaTypeRestriction", 17), ("finPrinterInputTraySupported", 18), ("finPreviousFinishingOperation", 19), ("finNextFinishingOperation", 20), ("stitchingType", 30), ("stitchingDirection", 31), ("foldingType", 40), ("bindingType", 50), ("punchHoleType", 80), ("punchHoleSizeLongDim", 81), ("punchHoleSizeShortDim", 82), ("punchPattern", 83), ("slittingType", 100), ("wrappingType", 130), ("stackOutputType", 160), ("stackOffset", 161), ("stackRotation", 162))

class FinEdgeTC(TextualConvention, Integer32):
    description = 'Specifies an edge for a Finishing Process.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(3, 4, 5, 6))
    namedValues = NamedValues(("topEdge", 3), ("bottomEdge", 4), ("leftEdge", 5), ("rightEdge", 6))

class FinStitchingTypeTC(TextualConvention, Integer32):
    description = 'The defined stitching type enumerations. For the edgeStitch and stapleDual enums, the finReferenceEdge attribute is recommended to define the edge to which the operation applies.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("stapleTopLeft", 4), ("stapleBottomLeft", 5), ("stapleTopRight", 6), ("stapleBottomRight", 7), ("saddleStitch", 8), ("edgeStitch", 9), ("stapleDual", 10))

class StitchingDirTypeTC(TextualConvention, Integer32):
    description = 'Defines the direction, relative to the top sheet in the output subunit, that the stitching operation was performed. For a topDown(3) process, the staple will be clinched on the bottom of the stack. This parameter can be used to determine what order the pages of a booklet are to be printed such that the staple clinch will be on the inside of the resulting booklet.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4))
    namedValues = NamedValues(("unknown", 2), ("topDown", 3), ("bottomUp", 4))

class StitchingAngleTypeTC(TextualConvention, Integer32):
    description = "This enumeration provides a description of the angular orientation of each stitch in a single or multiple stitching operation, relative to the 'X' axis. As with all finishing operations, the 'X' axis is always relative to the portrait orientation of the document regardless of the orientation of the printed image. This enum is primarily applicable to corner stitching operations."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 2), ("horizontal", 3), ("vertical", 4), ("slanted", 5))

class FinFoldingTypeTC(TextualConvention, Integer32):
    description = 'The defined folding device process enumerations.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("zFold", 3), ("halfFold", 4), ("letterFold", 5))

class FinBindingTypeTC(TextualConvention, Integer32):
    description = 'The defined binding type enumerations.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("tape", 4), ("plastic", 5), ("velo", 6), ("perfect", 7), ("spiral", 8), ("adhesive", 9), ("comb", 10), ("padding", 11))

class FinPunchHoleTypeTC(TextualConvention, Integer32):
    description = 'The defined hole type punch process enumerations.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("round", 3), ("oblong", 4), ("square", 5), ("rectangular", 6), ("star", 7))

class FinPunchPatternTC(TextualConvention, Integer32):
    description = 'The defined hole pattern punch process enumerations.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("twoHoleUSTop", 4), ("threeHoleUS", 5), ("twoHoleDIN", 6), ("fourHoleDIN", 7), ("twentyTwoHoleUS", 8), ("nineteenHoleUS", 9), ("twoHoleMetric", 10), ("swedish4Hole", 11), ("twoHoleUSSide", 12), ("fiveHoleUS", 13), ("sevenHoleUS", 14), ("mixed7H4S", 15), ("norweg6Hole", 16), ("metric26Hole", 17), ("metric30Hole", 18))

class FinSlittingTypeTC(TextualConvention, Integer32):
    description = 'The defined slitting type enumerations.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("slitAndSeparate", 4), ("slitAndMerge", 5))

class FinWrappingTypeTC(TextualConvention, Integer32):
    description = 'The defined wrapping device process enumerations.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("shrinkWrap", 4), ("paperWrap", 5))

class FinStackOutputTypeTC(TextualConvention, Integer32):
    description = 'The defined stack output type enumerations.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("straight", 4), ("offset", 5), ("crissCross", 6))

finDevice = MibIdentifier((1, 3, 6, 1, 2, 1, 43, 30))
finDeviceTable = MibTable((1, 3, 6, 1, 2, 1, 43, 30, 1), )
if mibBuilder.loadTexts: finDeviceTable.setStatus('current')
if mibBuilder.loadTexts: finDeviceTable.setDescription('This table defines the finishing device subunits, including information regarding possible configuration options and the status for each finisher device subunit.')
finDeviceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 43, 30, 1, 1), ).setIndexNames((0, "HOST-RESOURCES-MIB", "hrDeviceIndex"), (0, "Finisher-MIB", "finDeviceIndex"))
if mibBuilder.loadTexts: finDeviceEntry.setStatus('current')
if mibBuilder.loadTexts: finDeviceEntry.setDescription('There is an entry in the finishing device table for each possible finisher process.')
finDeviceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: finDeviceIndex.setStatus('current')
if mibBuilder.loadTexts: finDeviceIndex.setDescription('A unique value used to identify a finisher process. Although these values may change due to a major reconfiguration of the printer system (e.g. the addition of new finishing processes), the values are normally expected to remain stable across successive power cycles.')
finDeviceType = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 2), FinDeviceTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: finDeviceType.setStatus('current')
if mibBuilder.loadTexts: finDeviceType.setDescription('Defines the type of finishing process associated with this table row entry.')
finDevicePresentOnOff = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 3), PresentOnOff().clone('notPresent')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finDevicePresentOnOff.setStatus('current')
if mibBuilder.loadTexts: finDevicePresentOnOff.setDescription('Indicates if this finishing device subunit is available and whether the device subunit is enabled.')
finDeviceCapacityUnit = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 4), PrtCapacityUnitTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: finDeviceCapacityUnit.setStatus('current')
if mibBuilder.loadTexts: finDeviceCapacityUnit.setDescription('The unit of measure for specifying the capacity of this finisher device subunit.')
finDeviceMaxCapacity = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 2147483647)).clone(-2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finDeviceMaxCapacity.setStatus('current')
if mibBuilder.loadTexts: finDeviceMaxCapacity.setDescription('The maximum capacity of this finisher device subunit in finDeviceCapacityUnits. If the device can reliably sense this value, the value is sensed by the finisher device and is read-only: otherwise the value may be written by a management or control console application. The value (-1) means other and specifically indicates that the device places no restrictions on this parameter. The value (-2) means unknown.')
finDeviceCurrentCapacity = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 2147483647)).clone(-2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finDeviceCurrentCapacity.setStatus('current')
if mibBuilder.loadTexts: finDeviceCurrentCapacity.setDescription('The current capacity of this finisher device subunit in finDeviceCapacityUnits. If the device can reliably sense this value, the value is sensed by the finisher and is read-only: otherwise the value may be written by a management or control console application. The value (-1) means other and specifically indicates that the device places no restrictions on this parameter. The value (-2) means unknown.')
finDeviceAssociatedMediaPaths = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: finDeviceAssociatedMediaPaths.setStatus('current')
if mibBuilder.loadTexts: finDeviceAssociatedMediaPaths.setDescription('Indicates the media paths which can supply media for this finisher device. The value of this object is a bit map in an octet string with each position representing the value of a prtMediaPathIndex. For a media path that can be a source for this finisher device subunit, the bit position equal to one less than the value of prtMediaPathIndex will be set. The bits are numbered starting with the most significant bit of the first byte being bit 0, the least significant bit of the first byte being bit 7, the most significant of the second byte being bit 8, and so on.')
finDeviceAssociatedOutputs = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: finDeviceAssociatedOutputs.setStatus('current')
if mibBuilder.loadTexts: finDeviceAssociatedOutputs.setDescription('Indicates the printer output subunits this finisher device subunit services. The value of this object is a bit map in an octet string with each position representing the value of a prtOutputIndex. For an output subunit that is serviced by this finisher device subunit, the bit position equal to to one less than the value of prtOutputIndex will be set. The bits are numbered starting with the most significant bit of the first byte being bit 0, the least significant bit of the first byte being bit 7, the most significant of the second byte being bit 8, and so on.')
finDeviceStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 9), PrtSubUnitStatusTC().clone(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: finDeviceStatus.setStatus('current')
if mibBuilder.loadTexts: finDeviceStatus.setDescription('Indicates the current status of this finisher device subunit.')
finDeviceDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: finDeviceDescription.setStatus('current')
if mibBuilder.loadTexts: finDeviceDescription.setDescription('A free form text description of this device subunit in the localization specified by prtGeneralCurrentLocalization.')
finSupply = MibIdentifier((1, 3, 6, 1, 2, 1, 43, 31))
finSupplyTable = MibTable((1, 3, 6, 1, 2, 1, 43, 31, 1), )
if mibBuilder.loadTexts: finSupplyTable.setStatus('current')
if mibBuilder.loadTexts: finSupplyTable.setDescription('Each unique source of supply is an entry in the finisher supply table. Each supply entry has its own characteristics associated with it such as colorant and current supply level.')
finSupplyEntry = MibTableRow((1, 3, 6, 1, 2, 1, 43, 31, 1, 1), ).setIndexNames((0, "HOST-RESOURCES-MIB", "hrDeviceIndex"), (0, "Finisher-MIB", "finSupplyIndex"))
if mibBuilder.loadTexts: finSupplyEntry.setStatus('current')
if mibBuilder.loadTexts: finSupplyEntry.setDescription('A list of finisher devices, with their associated supplies and supplies characteristics.')
finSupplyIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: finSupplyIndex.setStatus('current')
if mibBuilder.loadTexts: finSupplyIndex.setDescription('A unique value used by a finisher to identify this supply container/receptacle. Although these values may change due to a major reconfiguration of the finisher (e.g. the addition of new supply sources to the finisher), values are normally expected to remain stable across successive power cycles.')
finSupplyDeviceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyDeviceIndex.setStatus('current')
if mibBuilder.loadTexts: finSupplyDeviceIndex.setDescription('The value of finDeviceIndex corresponding to the finishing device subunit with which this finisher supply is associated.')
finSupplyClass = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 3), PrtMarkerSuppliesClassTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyClass.setStatus('current')
if mibBuilder.loadTexts: finSupplyClass.setDescription('This value indicates whether this supply entity represents a supply that is consumed or a container that is filled.')
finSupplyType = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 4), PrtMarkerSuppliesTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyType.setStatus('current')
if mibBuilder.loadTexts: finSupplyType.setDescription('The type of this supply.')
finSupplyDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyDescription.setStatus('current')
if mibBuilder.loadTexts: finSupplyDescription.setDescription('The description of this supply/receptacle in text useful for operators and management applications and in the localization specified by prtGeneralCurrentLocalization.')
finSupplyUnit = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 6), PrtMarkerSuppliesSupplyUnitTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyUnit.setStatus('current')
if mibBuilder.loadTexts: finSupplyUnit.setDescription('Unit of measure of this finisher supply container or receptacle.')
finSupplyMaxCapacity = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 2147483647)).clone(-2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finSupplyMaxCapacity.setStatus('current')
if mibBuilder.loadTexts: finSupplyMaxCapacity.setDescription('The maximum capacity of this supply container/receptacle expressed in Supply Units. If this supply container/ receptacle can reliably sense this value, the value is sensed and is read-only; otherwise the value may be written by a control panel or management application. The value (-1) means other and places no restrictions on this parameter. The value (-2) means unknown.')
finSupplyCurrentLevel = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 8), Integer32().clone(-2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finSupplyCurrentLevel.setStatus('current')
if mibBuilder.loadTexts: finSupplyCurrentLevel.setDescription('The current level if this supply is a container; the remaining space if this supply is a receptacle. If this supply container/receptacle can reliably sense this value, the value is sensed and is read-only; otherwise the value may be written by a control panel or management application. The value (-1) means other and places no restrictions on this parameter. The value (-2) means unknown. A value of (-3) means that the printer knows there is some supply or remaining space.')
finSupplyColorName = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyColorName.setStatus('current')
if mibBuilder.loadTexts: finSupplyColorName.setDescription('The name of the color of this colorant using standardized string names from ISO 10175 (DPA) and ISO 10180 (SPDL) which are: other, unknown, white, red, green, blue, cyan, magenta, yellow and black. Implementors may add additional string values. The naming conventions in ISO 9070 are recommended in order to avoid potential name clashes.')
finSupplyMediaInput = MibIdentifier((1, 3, 6, 1, 2, 1, 43, 32))
finSupplyMediaInputTable = MibTable((1, 3, 6, 1, 2, 1, 43, 32, 1), )
if mibBuilder.loadTexts: finSupplyMediaInputTable.setStatus('current')
if mibBuilder.loadTexts: finSupplyMediaInputTable.setDescription('The input subunits associated with a finisher supply media are each represented by an entry in this table.')
finSupplyMediaInputEntry = MibTableRow((1, 3, 6, 1, 2, 1, 43, 32, 1, 1), ).setIndexNames((0, "HOST-RESOURCES-MIB", "hrDeviceIndex"), (0, "Finisher-MIB", "finSupplyMediaInputIndex"))
if mibBuilder.loadTexts: finSupplyMediaInputEntry.setStatus('current')
if mibBuilder.loadTexts: finSupplyMediaInputEntry.setDescription('A list of finisher supply media input subunit features and characteristics.')
finSupplyMediaInputIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: finSupplyMediaInputIndex.setStatus('current')
if mibBuilder.loadTexts: finSupplyMediaInputIndex.setDescription('A unique value used by a finisher to identify this supply media input subunit. Although these values may change due to a major reconfiguration of the finisher (e.g. the addition of new supply media input sources to the finisher), values are normally expected to remain stable across successive power cycles.')
finSupplyMediaInputDeviceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyMediaInputDeviceIndex.setStatus('current')
if mibBuilder.loadTexts: finSupplyMediaInputDeviceIndex.setDescription('The value of finDeviceIndex corresponding to the finishing device subunit with which this finisher media supply is associated.')
finSupplyMediaInputSupplyIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyMediaInputSupplyIndex.setStatus('current')
if mibBuilder.loadTexts: finSupplyMediaInputSupplyIndex.setDescription('The value of finSupplyIndex corresponding to the finishing supply subunit with which this finisher media supply is associated.')
finSupplyMediaInputType = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 4), PrtInputTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyMediaInputType.setStatus('current')
if mibBuilder.loadTexts: finSupplyMediaInputType.setDescription('The type of technology (discriminated primarily according to the feeder mechanism type) employed by the input subunit.')
finSupplyMediaInputDimUnit = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 5), PrtMediaUnitTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyMediaInputDimUnit.setStatus('current')
if mibBuilder.loadTexts: finSupplyMediaInputDimUnit.setDescription('The unit of measure for specifying dimensional values for this input device.')
finSupplyMediaInputMediaDimFeedDir = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finSupplyMediaInputMediaDimFeedDir.setStatus('current')
if mibBuilder.loadTexts: finSupplyMediaInputMediaDimFeedDir.setDescription('This object provides the value of the dimension in the feed direction of the media that is placed or will be placed in this input device. Feed dimension measurements are taken parallel to the feed direction of the device and measured in finSupplyMediaInputDimUnits. If this input device can reliably sense this value, the value is sensed and is read-only access. Otherwise the value is read-write access and may be written by management or control panel applications. The value (-1) means other and specifically indicates that this device places no restrictions on this parameter. The value (-2) indicates unknown. ')
finSupplyMediaInputMediaDimXFeedDir = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finSupplyMediaInputMediaDimXFeedDir.setStatus('current')
if mibBuilder.loadTexts: finSupplyMediaInputMediaDimXFeedDir.setDescription('This object provides the value of the dimension across the feed direction of the media that is placed or will be placed in this input device. The cross feed direction is ninety degrees relative to the feed direction on this device and measured in finSupplyMediaInputDimUnits. If this input device can reliably sense this value, the value is sensed and is read-only access. Otherwise the value is read-write access and may be written by management or control panel applications. The value (-1) means other and specifically indicates that this device places no restrictions on this parameter. The value (-2) indicates unknown. ')
finSupplyMediaInputStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 8), PrtSubUnitStatusTC().clone(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyMediaInputStatus.setStatus('current')
if mibBuilder.loadTexts: finSupplyMediaInputStatus.setDescription('This value indicates the current status of this input device.')
finSupplyMediaInputMediaName = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finSupplyMediaInputMediaName.setStatus('current')
if mibBuilder.loadTexts: finSupplyMediaInputMediaName.setDescription('The name of the current media contained in this input device. Examples are Engineering Manual Cover, Section A Tab Divider or any ISO standard names.')
finSupplyMediaInputName = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finSupplyMediaInputName.setStatus('current')
if mibBuilder.loadTexts: finSupplyMediaInputName.setDescription('The name assigned to this input subunit.')
finSupplyMediaInputDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyMediaInputDescription.setStatus('current')
if mibBuilder.loadTexts: finSupplyMediaInputDescription.setDescription('A free form text description of this input subunit in the localization specified by prtGeneralCurrentLocalization.')
finSupplyMediaInputSecurity = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 12), PresentOnOff()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finSupplyMediaInputSecurity.setStatus('current')
if mibBuilder.loadTexts: finSupplyMediaInputSecurity.setDescription('Indicates if this subunit has some security associated with it.')
finSupplyMediaInputMediaWeight = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finSupplyMediaInputMediaWeight.setStatus('current')
if mibBuilder.loadTexts: finSupplyMediaInputMediaWeight.setDescription('The weight of the media associated with this Input device in grams per meter squared. The value (-1) means other and specifically indicates that the device places no restriction on this parameter. The value (-2) means unknown. This object can be used to calculate the weight of individual pages processed by the document finisher. This value, when multiplied by the number of pages in a finished set, can be used to calculate the weight of a set before it is inserted into a mailing envelope.')
finSupplyMediaInputMediaThickness = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finSupplyMediaInputMediaThickness.setStatus('current')
if mibBuilder.loadTexts: finSupplyMediaInputMediaThickness.setDescription('This object identifies the thickness of the input media processed by this document input subunit measured in micrometers. This value may be used by devices (or operators) to set up proper machine tolerances for the feeder operation. The value (-2) indicates that the media thickness is unknown or not used in the setup for this input subunit.')
finSupplyMediaInputMediaType = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finSupplyMediaInputMediaType.setStatus('current')
if mibBuilder.loadTexts: finSupplyMediaInputMediaType.setDescription('The name of the type of medium associated with this input subunit. Valid values are standardized strings from ISO 10175 (DPA) and ISO 10180 (SPDL) which are: stationary, transparency, envelope, envelope-plain, envelope window, continuous-long, continuous-short, tab-stock, labels, multi-layer.')
finDeviceAttribute = MibIdentifier((1, 3, 6, 1, 2, 1, 43, 33))
finDeviceAttributeTable = MibTable((1, 3, 6, 1, 2, 1, 43, 33, 1), )
if mibBuilder.loadTexts: finDeviceAttributeTable.setStatus('current')
if mibBuilder.loadTexts: finDeviceAttributeTable.setDescription('The attribute table defines special parameters that are applicable only to a minority of the finisher devices. An attribute table entry is used, rather than unique objects, to minimize the number of MIB objects and to allow for expansion without the addition of MIB objects. Each finisher device is represented by a separate row in the device subunit attribute table.')
finDeviceAttributeEntry = MibTableRow((1, 3, 6, 1, 2, 1, 43, 33, 1, 1), ).setIndexNames((0, "HOST-RESOURCES-MIB", "hrDeviceIndex"), (0, "Finisher-MIB", "finDeviceIndex"), (0, "Finisher-MIB", "finDeviceAttributeTypeIndex"), (0, "Finisher-MIB", "finDeviceAttributeInstanceIndex"))
if mibBuilder.loadTexts: finDeviceAttributeEntry.setStatus('current')
if mibBuilder.loadTexts: finDeviceAttributeEntry.setDescription('Each entry defines a finisher function parameter that cannot be represented by an object in the finisher device subunit table.')
finDeviceAttributeTypeIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 33, 1, 1, 1), FinAttributeTypeTC())
if mibBuilder.loadTexts: finDeviceAttributeTypeIndex.setStatus('current')
if mibBuilder.loadTexts: finDeviceAttributeTypeIndex.setDescription('Defines the attribute type represented by this row.')
finDeviceAttributeInstanceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 33, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: finDeviceAttributeInstanceIndex.setStatus('current')
if mibBuilder.loadTexts: finDeviceAttributeInstanceIndex.setDescription('An index that allows the discrimination of an attribute instance when the same attribute occurs multiple times for a specific instance of a finisher function. The value of this index shall be 1 if only a single instance of the attribute occurs for the specific finisher function.')
finDeviceAttributeValueAsInteger = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 33, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 2147483647)).clone(-2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finDeviceAttributeValueAsInteger.setStatus('current')
if mibBuilder.loadTexts: finDeviceAttributeValueAsInteger.setDescription("Defines the integer value of the attribute. The value of the attribute is represented as an integer if the finAttributeTypeTC description for the attribute has the tag 'INTEGER:'. Depending upon the attribute enum definition, this object may be either an integer, a counter, an index, or an enum. Attributes for which the concept of an integer value is not meaningful SHALL return a value of -1 for this attribute.")
finDeviceAttributeValueAsOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 33, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finDeviceAttributeValueAsOctets.setStatus('current')
if mibBuilder.loadTexts: finDeviceAttributeValueAsOctets.setDescription("Contains the octet string value of the attribute. The value of the attribute is represented as a string if the finAttributeTypeTC description for the attribute has the tag 'OCTETS:'. Depending upon the attribute enum definition, this object may be either a coded character set string (text) or a binary octet string. Attributes for which the concept of an octet string value is not meaningful SHALL contain a zero length string.")
finMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 43, 2, 3)).setObjects(("Finisher-MIB", "finDeviceGroup"), ("Finisher-MIB", "finSupplyGroup"), ("Finisher-MIB", "finDeviceAttributeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    finMIBCompliance = finMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: finMIBCompliance.setDescription('The compliance statement for agents that implement the finisher MIB.')
finMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 43, 2, 4))
finDeviceGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 43, 2, 4, 1)).setObjects(("Finisher-MIB", "finDeviceType"), ("Finisher-MIB", "finDevicePresentOnOff"), ("Finisher-MIB", "finDeviceCapacityUnit"), ("Finisher-MIB", "finDeviceMaxCapacity"), ("Finisher-MIB", "finDeviceCurrentCapacity"), ("Finisher-MIB", "finDeviceAssociatedMediaPaths"), ("Finisher-MIB", "finDeviceAssociatedOutputs"), ("Finisher-MIB", "finDeviceStatus"), ("Finisher-MIB", "finDeviceDescription"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    finDeviceGroup = finDeviceGroup.setStatus('current')
if mibBuilder.loadTexts: finDeviceGroup.setDescription('The finisher device group.')
finSupplyGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 43, 2, 4, 2)).setObjects(("Finisher-MIB", "finSupplyDeviceIndex"), ("Finisher-MIB", "finSupplyClass"), ("Finisher-MIB", "finSupplyType"), ("Finisher-MIB", "finSupplyDescription"), ("Finisher-MIB", "finSupplyUnit"), ("Finisher-MIB", "finSupplyMaxCapacity"), ("Finisher-MIB", "finSupplyCurrentLevel"), ("Finisher-MIB", "finSupplyColorName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    finSupplyGroup = finSupplyGroup.setStatus('current')
if mibBuilder.loadTexts: finSupplyGroup.setDescription('The finisher supply group.')
finSupplyMediaInputGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 43, 2, 4, 3)).setObjects(("Finisher-MIB", "finSupplyMediaInputDeviceIndex"), ("Finisher-MIB", "finSupplyMediaInputSupplyIndex"), ("Finisher-MIB", "finSupplyMediaInputType"), ("Finisher-MIB", "finSupplyMediaInputDimUnit"), ("Finisher-MIB", "finSupplyMediaInputMediaDimFeedDir"), ("Finisher-MIB", "finSupplyMediaInputMediaDimXFeedDir"), ("Finisher-MIB", "finSupplyMediaInputStatus"), ("Finisher-MIB", "finSupplyMediaInputMediaName"), ("Finisher-MIB", "finSupplyMediaInputName"), ("Finisher-MIB", "finSupplyMediaInputDescription"), ("Finisher-MIB", "finSupplyMediaInputSecurity"), ("Finisher-MIB", "finSupplyMediaInputMediaWeight"), ("Finisher-MIB", "finSupplyMediaInputMediaThickness"), ("Finisher-MIB", "finSupplyMediaInputMediaType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    finSupplyMediaInputGroup = finSupplyMediaInputGroup.setStatus('current')
if mibBuilder.loadTexts: finSupplyMediaInputGroup.setDescription('The finisher supply, media input group.')
finDeviceAttributeGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 43, 2, 4, 4)).setObjects(("Finisher-MIB", "finDeviceAttributeValueAsInteger"), ("Finisher-MIB", "finDeviceAttributeValueAsOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    finDeviceAttributeGroup = finDeviceAttributeGroup.setStatus('current')
if mibBuilder.loadTexts: finDeviceAttributeGroup.setDescription('The finisher device attribute group.')
mibBuilder.exportSymbols("Finisher-MIB", finDeviceEntry=finDeviceEntry, FinBindingTypeTC=FinBindingTypeTC, finDeviceDescription=finDeviceDescription, finDevicePresentOnOff=finDevicePresentOnOff, finSupplyMediaInputName=finSupplyMediaInputName, finSupplyMediaInputMediaWeight=finSupplyMediaInputMediaWeight, finDeviceAttributeTypeIndex=finDeviceAttributeTypeIndex, finDeviceAttributeGroup=finDeviceAttributeGroup, finSupplyMediaInputType=finSupplyMediaInputType, finDeviceAttribute=finDeviceAttribute, finSupplyMaxCapacity=finSupplyMaxCapacity, FinDeviceTypeTC=FinDeviceTypeTC, FinPunchPatternTC=FinPunchPatternTC, finSupplyMediaInputMediaName=finSupplyMediaInputMediaName, finSupplyCurrentLevel=finSupplyCurrentLevel, finSupplyUnit=finSupplyUnit, finDeviceAttributeTable=finDeviceAttributeTable, finDeviceGroup=finDeviceGroup, finSupply=finSupply, finSupplyType=finSupplyType, finDeviceAttributeEntry=finDeviceAttributeEntry, finisherMIB=finisherMIB, finDeviceCapacityUnit=finDeviceCapacityUnit, finSupplyMediaInputDeviceIndex=finSupplyMediaInputDeviceIndex, finSupplyMediaInputDescription=finSupplyMediaInputDescription, finSupplyMediaInputMediaType=finSupplyMediaInputMediaType, finSupplyMediaInputMediaThickness=finSupplyMediaInputMediaThickness, FinAttributeTypeTC=FinAttributeTypeTC, finDeviceAttributeValueAsOctets=finDeviceAttributeValueAsOctets, finSupplyMediaInputMediaDimFeedDir=finSupplyMediaInputMediaDimFeedDir, finSupplyMediaInputMediaDimXFeedDir=finSupplyMediaInputMediaDimXFeedDir, finDeviceAttributeValueAsInteger=finDeviceAttributeValueAsInteger, finSupplyMediaInputIndex=finSupplyMediaInputIndex, finSupplyMediaInputSecurity=finSupplyMediaInputSecurity, finSupplyMediaInputSupplyIndex=finSupplyMediaInputSupplyIndex, finSupplyColorName=finSupplyColorName, finSupplyDeviceIndex=finSupplyDeviceIndex, FinFoldingTypeTC=FinFoldingTypeTC, finDeviceCurrentCapacity=finDeviceCurrentCapacity, FinEdgeTC=FinEdgeTC, finSupplyEntry=finSupplyEntry, finSupplyDescription=finSupplyDescription, FinPunchHoleTypeTC=FinPunchHoleTypeTC, FinWrappingTypeTC=FinWrappingTypeTC, finDeviceAssociatedMediaPaths=finDeviceAssociatedMediaPaths, finSupplyMediaInputStatus=finSupplyMediaInputStatus, finSupplyMediaInputGroup=finSupplyMediaInputGroup, finDeviceType=finDeviceType, finSupplyGroup=finSupplyGroup, finSupplyTable=finSupplyTable, finSupplyMediaInputDimUnit=finSupplyMediaInputDimUnit, finDeviceAssociatedOutputs=finDeviceAssociatedOutputs, finMIBCompliance=finMIBCompliance, finDeviceTable=finDeviceTable, finMIBGroups=finMIBGroups, finDeviceMaxCapacity=finDeviceMaxCapacity, StitchingAngleTypeTC=StitchingAngleTypeTC, FinStackOutputTypeTC=FinStackOutputTypeTC, finDeviceStatus=finDeviceStatus, finSupplyIndex=finSupplyIndex, finSupplyMediaInput=finSupplyMediaInput, finDeviceIndex=finDeviceIndex, finSupplyClass=finSupplyClass, finDeviceAttributeInstanceIndex=finDeviceAttributeInstanceIndex, FinStitchingTypeTC=FinStitchingTypeTC, PYSNMP_MODULE_ID=finisherMIB, FinSlittingTypeTC=FinSlittingTypeTC, finDevice=finDevice, finSupplyMediaInputEntry=finSupplyMediaInputEntry, finSupplyMediaInputTable=finSupplyMediaInputTable, StitchingDirTypeTC=StitchingDirTypeTC)
