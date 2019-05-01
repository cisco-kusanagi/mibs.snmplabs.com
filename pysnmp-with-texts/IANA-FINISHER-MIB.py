#
# PySNMP MIB module IANA-FINISHER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IANA-FINISHER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:50:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Gauge32, ObjectIdentity, ModuleIdentity, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, iso, mib_2, Unsigned32, IpAddress, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "ObjectIdentity", "ModuleIdentity", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "iso", "mib-2", "Unsigned32", "IpAddress", "TimeTicks", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ianafinisherMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 110))
ianafinisherMIB.setRevisions(('2014-05-22 00:00', '2009-11-03 00:00', '2004-06-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ianafinisherMIB.setRevisionsDescriptions(('Updated contact info.', 'Added plasticMultiRing(12).', 'Original version, published in coordination with Finisher MIB (RFC 3806).',))
if mibBuilder.loadTexts: ianafinisherMIB.setLastUpdated('201405220000Z')
if mibBuilder.loadTexts: ianafinisherMIB.setOrganization('IANA')
if mibBuilder.loadTexts: ianafinisherMIB.setContactInfo('Internet Assigned Numbers Authority Postal: ICANN 12025 Waterfront Drive, Suite 300 Los Angeles, CA 90094-2536 Tel: +1 310-301-5800 E-Mail: iana&iana.org')
if mibBuilder.loadTexts: ianafinisherMIB.setDescription('This MIB module defines a set of finishing-related TEXTUAL-CONVENTIONs for use in Finisher MIB (RFC 3806) and other MIBs which need to specify finishing mechanism details. Any additions or changes to the contents of this MIB module require either publication of an RFC, or Designated Expert Review as defined in RFC 2434, Guidelines for Writing an IANA Considerations Section in RFCs. The Designated Expert will be selected by the IESG Area Director(s) of the Applications Area. Copyright (C) The Internet Society (2004). The initial version of this MIB module was published in RFC 3806. For full legal notices see the RFC itself or see: http://www.ietf.org/copyrights/ianamib.html')
class FinDeviceTypeTC(TextualConvention, Integer32):
    description = 'The defined finishing device subunit process enumerations.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("stitcher", 3), ("folder", 4), ("binder", 5), ("trimmer", 6), ("dieCutter", 7), ("puncher", 8), ("perforater", 9), ("slitter", 10), ("separationCutter", 11), ("imprinter", 12), ("wrapper", 13), ("bander", 14), ("makeEnvelope", 15), ("stacker", 16), ("sheetRotator", 17), ("inserter", 18))

class FinAttributeTypeTC(TextualConvention, Integer32):
    description = 'This TEXTUAL-CONVENTION defines the set of enums for use in the finDeviceAttributeTable. See section 5.7 for the complete specification of each attribute.'
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

class FinStitchingDirTypeTC(TextualConvention, Integer32):
    description = 'Defines the direction, relative to the top sheet in the output subunit, that the stitching operation was performed. For a topDown(3) process, the staple will be clinched on the bottom of the stack. This parameter can be used to determine what order the pages of a booklet are to be printed such that the staple clinch will be on the inside of the resulting booklet.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4))
    namedValues = NamedValues(("unknown", 2), ("topDown", 3), ("bottomUp", 4))

class FinStitchingAngleTypeTC(TextualConvention, Integer32):
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
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("tape", 4), ("plastic", 5), ("velo", 6), ("perfect", 7), ("spiral", 8), ("adhesive", 9), ("comb", 10), ("padding", 11), ("plasticMultiRing", 12))

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

mibBuilder.exportSymbols("IANA-FINISHER-MIB", FinEdgeTC=FinEdgeTC, FinPunchHoleTypeTC=FinPunchHoleTypeTC, FinDeviceTypeTC=FinDeviceTypeTC, FinFoldingTypeTC=FinFoldingTypeTC, FinStitchingAngleTypeTC=FinStitchingAngleTypeTC, FinAttributeTypeTC=FinAttributeTypeTC, FinStitchingTypeTC=FinStitchingTypeTC, FinSlittingTypeTC=FinSlittingTypeTC, FinBindingTypeTC=FinBindingTypeTC, FinWrappingTypeTC=FinWrappingTypeTC, ianafinisherMIB=ianafinisherMIB, FinStackOutputTypeTC=FinStackOutputTypeTC, PYSNMP_MODULE_ID=ianafinisherMIB, FinPunchPatternTC=FinPunchPatternTC, FinStitchingDirTypeTC=FinStitchingDirTypeTC)
