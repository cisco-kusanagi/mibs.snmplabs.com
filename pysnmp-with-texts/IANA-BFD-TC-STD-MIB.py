#
# PySNMP MIB module IANA-BFD-TC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IANA-BFD-TC-STD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:37:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Bits, TimeTicks, NotificationType, ModuleIdentity, Gauge32, Unsigned32, Counter64, IpAddress, ObjectIdentity, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Bits", "TimeTicks", "NotificationType", "ModuleIdentity", "Gauge32", "Unsigned32", "Counter64", "IpAddress", "ObjectIdentity", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "mib-2")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaBfdTCStdMib = ModuleIdentity((1, 3, 6, 1, 2, 1, 224))
ianaBfdTCStdMib.setRevisions(('2014-08-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ianaBfdTCStdMib.setRevisionsDescriptions(('Initial version. Published as RFC 7330.',))
if mibBuilder.loadTexts: ianaBfdTCStdMib.setLastUpdated('201408120000Z')
if mibBuilder.loadTexts: ianaBfdTCStdMib.setOrganization('IANA')
if mibBuilder.loadTexts: ianaBfdTCStdMib.setContactInfo('Internet Assigned Numbers Authority Postal: 12025 Waterfront Drive, Suite 300 Los Angeles, CA 90094-2536 Tel: +1 310 301 5800 EMail: iana&iana.org')
if mibBuilder.loadTexts: ianaBfdTCStdMib.setDescription("Copyright (c) 2014 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, is permitted pursuant to, and subject to the license terms contained in, the Simplified BSD License set forth in Section 4.c of the IETF Trust's Legal Provisions Relating to IETF Documents (http://trustee.ietf.org/license-info).")
class IANAbfdDiagTC(TextualConvention, Integer32):
    reference = 'Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD), RFC 5880, June 2010. Allan, D., Swallow, G., and Drake, J., Proactive Connectivity Verification, Continuity Check, and Remote Defect Indication for the MPLS Transport Profile, RFC 6428, November 2011.'
    description = 'A common BFD diagnostic code.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("noDiagnostic", 0), ("controlDetectionTimeExpired", 1), ("echoFunctionFailed", 2), ("neighborSignaledSessionDown", 3), ("forwardingPlaneReset", 4), ("pathDown", 5), ("concatenatedPathDown", 6), ("administrativelyDown", 7), ("reverseConcatenatedPathDown", 8), ("misConnectivityDefect", 9))

class IANAbfdSessTypeTC(TextualConvention, Integer32):
    reference = 'Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD), RFC 5880, June 2010. Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD) for IPv4 and IPv6 (Single Hop), RFC 5881, June 2010. Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD) for Multihop Paths, RFC 5883, June 2010.'
    description = 'BFD session type'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("singleHop", 1), ("multiHopTotallyArbitraryPaths", 2), ("multiHopOutOfBandSignaling", 3), ("multiHopUnidirectionalLinks", 4))

class IANAbfdSessOperModeTC(TextualConvention, Integer32):
    reference = 'Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD), RFC 5880, June 2010.'
    description = 'BFD session operating mode'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("asyncModeWEchoFunction", 1), ("asynchModeWOEchoFunction", 2), ("demandModeWEchoFunction", 3), ("demandModeWOEchoFunction", 4))

class IANAbfdSessStateTC(TextualConvention, Integer32):
    reference = 'Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD), RFC 5880, June 2010.'
    description = 'BFD session state. State failing(5) is only applicable if corresponding session is running in BFD version 0.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("adminDown", 1), ("down", 2), ("init", 3), ("up", 4), ("failing", 5))

class IANAbfdSessAuthenticationTypeTC(TextualConvention, Integer32):
    reference = 'Sections 4.2 - 4.4 from Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD), RFC 5880, June 2010.'
    description = 'BFD authentication type'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("noAuthentication", -1), ("reserved", 0), ("simplePassword", 1), ("keyedMD5", 2), ("meticulousKeyedMD5", 3), ("keyedSHA1", 4), ("meticulousKeyedSHA1", 5))

class IANAbfdSessAuthenticationKeyTC(TextualConvention, OctetString):
    reference = 'Sections 4.2 - 4.4 from Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD), RFC 5880, June 2010.'
    description = "BFD authentication key type. An IANAbfdSessAuthenticationKeyTC is always interpreted within the context of an IANAbfdSessAuthenticationTypeTC value. Every usage of the IANAbfdSessAuthenticationTypeTC textual convention is required to specify the IANAbfdSessAuthenticationKeyTC object that provides the context. It is suggested that the IANAbfdSessAuthenticationKeyTC object be logically registered before the object(s) that use the IANAbfdSessAuthenticationKeyTC textual convention, if they appear in the same logical row. The value of an IANAbfdSessAuthenticationKeyTC must always be consistent with the value of the associated IANAbfdSessAuthenticationTypeTC object. Attempts to set an IANAbfdSessAuthenticationKeyTC object to a value inconsistent with the associated IANAbfdSessAuthenticationTypeTC must fail with an inconsistentValue error. The following size constraints for an IANAbfdSessAuthenticationKeyTC object are defined for the associated IANAbfdSessAuthenticationTypeTC values show below: noAuthentication(-1): SIZE(0) reserved(0): SIZE(0) simplePassword(1): SIZE(1..16) keyedMD5(2): SIZE(16) meticulousKeyedMD5(3): SIZE(16) keyedSHA1(4): SIZE(20) meticulousKeyedSHA1(5): SIZE(20) When this textual convention is used as the syntax of an index object, there may be issues with the limit of 128 sub-identifiers specified in SMIv2, STD 58. In this case, the object definition MUST include a 'SIZE' clause to limit the number of potential instance sub-identifiers; otherwise, the applicable constraints MUST be stated in the appropriate conceptual row DESCRIPTION clauses, or in the surrounding documentation if there is no single DESCRIPTION clause that is appropriate."
    status = 'current'
    displayHint = '1x '
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 252)

mibBuilder.exportSymbols("IANA-BFD-TC-STD-MIB", IANAbfdDiagTC=IANAbfdDiagTC, PYSNMP_MODULE_ID=ianaBfdTCStdMib, IANAbfdSessTypeTC=IANAbfdSessTypeTC, IANAbfdSessAuthenticationKeyTC=IANAbfdSessAuthenticationKeyTC, IANAbfdSessOperModeTC=IANAbfdSessOperModeTC, IANAbfdSessAuthenticationTypeTC=IANAbfdSessAuthenticationTypeTC, ianaBfdTCStdMib=ianaBfdTCStdMib, IANAbfdSessStateTC=IANAbfdSessStateTC)
