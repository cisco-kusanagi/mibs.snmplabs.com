#
# PySNMP MIB module MULTI-MEDIA-MIB-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MULTI-MEDIA-MIB-TC
# Produced by pysmi-0.3.4 at Wed May  1 13:21:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, ObjectIdentity, TimeTicks, NotificationType, Counter64, IpAddress, iso, Unsigned32, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "ObjectIdentity", "TimeTicks", "NotificationType", "Counter64", "IpAddress", "iso", "Unsigned32", "Integer32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mmRoot = MibIdentifier((0, 0, 8, 341, 1))
class MmUtf8String(TextualConvention, OctetString):
    description = 'To facilitate internationalization, this TC represents information taken from the ISO/IEC IS 10646-1 character set, encoded as an octet string using the UTF-8 character encoding scheme described in RFC 2044 [8]. For strings in 7-bit US-ASCII, there is no impact since the UTF-8 representation is identical to the US-ASCII encoding.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class MmE164String(TextualConvention, OctetString):
    description = "A UTF-8 string limited to the character set defined for E.164, '0123456789*#,<quote>' "
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class MmTAddressTag(TextualConvention, Integer32):
    description = 'A tag to identify the type of the transport address contained in the TAddress textual convention. The values correlate to the TransporTAddress defined in the H.225.0 V2 ITU protocol specification. The tag indicates how to interpret the value of a TAddress data type defined in this specification. All TAddress values are in network byte order TAddress size TAddress contents ipv4 6 octets IPv4 (4 octets), port (2) ipv6 18 IPv6 (16), port (2) ipx 12 net (4), node (6), port (2) nsap 1-20 nsap(1-20) netbios 16 netbios(16) '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 0), ("ipv4", 1), ("ipv6", 2), ("ipx", 3), ("nsap", 4), ("netbios", 5))

class MmGlobalIdentifier(TextualConvention, OctetString):
    reference = 'ITU H225.0 Version 2'
    description = 'A 16 octet field containing a unique identifier. The identifier contains the following fields: 60 bit nanosecond time (octets 1-7, low 4 bits of octet 8) 4 bit version (hi 4 bits of octet 8) 3 octet 0 (a variant field) 1 octet hi 2bits 0, low 6bits clock sequence. 6 octet MAC Address See Reference for generation of this value. '
    status = 'current'
    displayHint = '8d-9,3x,1d,2x:2x:2x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class MmAliasTag(TextualConvention, Integer32):
    description = 'A tag to identify the type of the Alias address contained in the MmAliasAddress data type. The values correlate to the AliasAddress defined in the H.225.0 V2 ITU protocol specification. The tag indicates how to interpret the value of an AliasAddress data type defined in that specification. AliasAddress contents other unknown e164 MmE164String h323Id MmUtf8String urlId MmUtf8String containing a URL transportId MmTAddressTag, TAddress emailId MmUtf8String containing e-mail address partyNumber contains PartyNumber '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 0), ("e164", 1), ("h323Id", 2), ("urlId", 3), ("transportId", 4), ("emailId", 5), ("partyNumber", 6))

class MmAliasAddress(TextualConvention, OctetString):
    reference = 'ITU H225.0 Version 2'
    description = 'A data type corresponding to AliasAddress defined in H.225.0. The value of an object of this type has the syntax and symantics identified by MmAliasTag. An object defined as MmAliasAddress must have a corresponding MmAliasTag object.'
    status = 'current'
    displayHint = '512a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 512)

class MmEndpointID(TextualConvention, OctetString):
    reference = 'ITU H225.0 Version 2'
    description = 'A data type corresponding to EndpointIdentifier defined in H.225.0.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class MmGatekeeperID(TextualConvention, OctetString):
    reference = 'ITU H225.0 Version 2'
    description = 'A data type corresponding to GatekeeperIdentifier defined in H.225.0.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class MmH225Crv(TextualConvention, Integer32):
    reference = 'ITU H225.0 Version 2'
    description = 'A data type corresponding to the Call Reference Value defined in H.225.0.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class MmTerminalAudioCapability(TextualConvention, Bits):
    reference = 'ITU H225.0 Version 2'
    description = 'This object represents the audio capabilities of a terminal device.'
    status = 'current'
    namedValues = NamedValues(("g711ALaw64KAudio", 0), ("g711ALaw56KAudio", 1), ("g711ULaw64KAudio", 2), ("g711ULaw56KAudio", 3), ("g722d64KAudio", 4), ("g722d56KAudio", 5), ("g722d48KAudio", 6), ("g728Audio", 7), ("g723d1d5d3KAudio", 8), ("g723d1d6d4KAudio", 9), ("g729Audio", 10))

class MmTerminalDataCapability(TextualConvention, Bits):
    reference = ''
    description = 'This object represents the data application capabilities of a terminal device.'
    status = 'current'
    namedValues = NamedValues(("t120", 0), ("dsmCc", 1), ("userData", 2), ("t84", 3), ("t434", 4), ("h224", 5), ("nlpid", 6), ("dsvdControl", 7), ("h222DataPartitioning", 8), ("t30fax", 9), ("t140", 10), ("others", 11))

class MmTerminalVideoCapability(TextualConvention, Bits):
    reference = ''
    description = 'This object represents the video capabilities of a terminal device.'
    status = 'current'
    namedValues = NamedValues(("h261CIFVideo", 0), ("h261QCIFVideo", 1), ("h263SQCIFVideo", 2), ("h263QCIFVideo", 3), ("h263CIFVideo", 4), ("h263CIF4Video", 5), ("h263CIF16Video", 6), ("h262SPMLSIFVideo", 7), ("h262SPML2SIFVideo", 8), ("h262SPML4SIFVideo", 9), ("h262MPMLSIFVideo", 10), ("h262MPML2SIFVideo", 11), ("h262MPML4SIFVideo", 12))

class MmTerminalLineRateCapability(TextualConvention, Bits):
    reference = ''
    description = 'This object represents the line rate capabilities of a terminal device.'
    status = 'current'
    namedValues = NamedValues(("bps64K", 0), ("bps2x64K", 1), ("bps3x64K", 2), ("bps4x64K", 3), ("bps5x64K", 4), ("bps6x64K", 5), ("bps384K", 6), ("bps2x384K", 7), ("bps3x384K", 8), ("bps5x384K", 9), ("bps1536K", 10), ("bps1920K", 11), ("bps128K", 12), ("bps192K", 13), ("bps256K", 14), ("bps320K", 15), ("bps512K", 16), ("bps768K", 17), ("bps1152K", 18), ("bps1452K", 19))

class MmControlsCommands(TextualConvention, Integer32):
    reference = ''
    description = 'A value that represents a command for an endpoint. 1. Other (for proprietary extensions) 2. Abrupt Restart (Drastic Restart) 3. Graceful Restart (Restart after all calls have terminated. Meanwhile, accept no calls) 4. Abrupt Shutdown (Drastic Restart) 5. Graceful Shutdown (Shutdown after all calls have terminated. Meanwhile, accept no calls) 6. Enter Quiescence Mode (Disable receiving of calls) 7. Exit Quiescence Mode (Enable receiving of calls) 8. Start Error/Log Reporting 9. Stop Error/Log Reporting 10. Reset Statistics 11. Run Diagnostic'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("other", 1), ("abruptRestart", 2), ("gracefulRestart", 3), ("abruptShutdown", 4), ("gracefulShutdown", 5), ("enterQuiescence", 6), ("exitQuiescence", 7), ("startLog", 8), ("stopLog", 9), ("resetStatistics", 10), ("runDiagnostic", 11))

class MmErrorSeverity(TextualConvention, Integer32):
    description = ' Error Severities from OSI Defined Values (X.733): Cleared - The clearing of one or more previously reported alarms, Indeterminate - The severity level cannot be determined, Critical - A service affecting condition has occurred and an immediate corrective action is required, Major - A service affecting condition has occurred and an urgent corrective action is required, Minor - A non-service affecting condition has occurred and corrective action should be taken to prevent a more serious condition, Warning - The detection of an potential or impending service affecting fault, before any significant effects have been felt. Action should be taken to further diagnose and correct the problem to prevent a more serious condition '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("cleared", 0), ("indeterminate", 1), ("critical", 2), ("major", 3), ("minor", 4), ("warning", 5))

class MmErrorProbableCause(TextualConvention, Integer32):
    description = ' Enumerated list of possible GW Errors: other(1), -- errors on a Connection qoSDegraded(2) - the quality of Service has been reduced, lossOfConn(3) - this entity has lost the connection, commProtocolError(4) - A communication protocol has been violated, alarmSignal(5) - An alarm condition exists on this connection performanceDegraded(6) - Service agreements or Service limits are outside of acceptable limits, -- errors on a Call callEstablishmentError (7) - the call could not be established, alarmOnIncomingConn(8) - An alarm condition exists on the ingress connection, this could be due to any one of the error types (1), (2), (4),(5), or (6) existing on the ingress connection, alarmOnOutgoingConn(9) - An alarm condition exists on the egress connection, this could be due to any one of the error types (1), (2), (4),(5), or (6) existing on the ingress connection, lossOfIncomingConn(10) - this entity has lost the ingress connection, lossOfOutgoingConn(11) - this entity has lost the ingress connection, -- errors on an entity componentFailure (12) - a physical resource, for example, a circuit, in this entity has failed, processingError(13) - an error in a software program, for example, a s/w version mismatch, congestion (14) - this entity has reached its capacity or is approaching it, powerProblem(15) - there is a problem with the power supply for one or more resources. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 16, 17, 18, 19, 20, 30, 31, 32, 33))
    namedValues = NamedValues(("other", 1), ("qoSDegraded", 2), ("lossOfConn", 3), ("commProtocolError", 4), ("alarmSignal", 5), ("performanceDegraded", 6), ("callEstablishmentError", 16), ("alarmOnIncomingConn", 17), ("alarmOnOutgoingConn", 18), ("lossOfIncomingConn", 19), ("lossOfOutgoingConn", 20), ("componentFailure", 30), ("processingError", 31), ("congestion", 32), ("powerProblem", 33))

class MmH323EndpointType(TextualConvention, Integer32):
    reference = 'ITU H.323'
    description = ' Terminal type represents the type of H.323 terminal: 50 - terminal without MC 60 - gateway without MC 70 - terminal with MC but without MP 80 - gateway with MC but without MP 120 - gatekeeper with MC but without MP 160 - MCU with MC but without MP 90 - gateway with MC and Data MP 130 - gatekeeper with MC and Data MP 170 - MCU with MC and Data MP 100 - gateway containing MC with Data and audio MP 140 - gatekeeper containing MC with Data and audio MP 180 - MCU containing MC with Data and audio MP 110 - gateway containing MC with Data, Audio and Video MP 150 - gatekeeper containing MC with Data, Audio and Video MP 190 - MCU containing MC with Data, Audio and Video MP 240 - entity with active MC . '
    status = 'current'

mmH323Root = ObjectIdentity((0, 0, 8, 341, 1, 1))
if mibBuilder.loadTexts: mmH323Root.setStatus('current')
if mibBuilder.loadTexts: mmH323Root.setDescription('Subtree for root of H323 mib modules.')
mmH320Root = ObjectIdentity((0, 0, 8, 341, 1, 2))
if mibBuilder.loadTexts: mmH320Root.setStatus('current')
if mibBuilder.loadTexts: mmH320Root.setDescription('Subtree for root of H320 mib modules.')
mmH245Root = ObjectIdentity((0, 0, 8, 341, 1, 3))
if mibBuilder.loadTexts: mmH245Root.setStatus('current')
if mibBuilder.loadTexts: mmH245Root.setDescription('Subtree for root of H245 mib modules.')
mmH323GatewayRoot = ObjectIdentity((0, 0, 8, 341, 1, 4))
if mibBuilder.loadTexts: mmH323GatewayRoot.setStatus('current')
if mibBuilder.loadTexts: mmH323GatewayRoot.setDescription('Subtree for root of H245 mib modules.')
class MmCallType(TextualConvention, Integer32):
    description = 'This value indicates the call type. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("pointToPoint", 1), ("oneToN", 2), ("nToOne", 3), ("nToN", 4))

mibBuilder.exportSymbols("MULTI-MEDIA-MIB-TC", mmH320Root=mmH320Root, MmAliasAddress=MmAliasAddress, MmTerminalDataCapability=MmTerminalDataCapability, MmUtf8String=MmUtf8String, mmH323Root=mmH323Root, MmTerminalLineRateCapability=MmTerminalLineRateCapability, MmTerminalVideoCapability=MmTerminalVideoCapability, MmTerminalAudioCapability=MmTerminalAudioCapability, MmControlsCommands=MmControlsCommands, MmE164String=MmE164String, mmRoot=mmRoot, MmGlobalIdentifier=MmGlobalIdentifier, MmEndpointID=MmEndpointID, MmCallType=MmCallType, MmErrorProbableCause=MmErrorProbableCause, MmH323EndpointType=MmH323EndpointType, MmTAddressTag=MmTAddressTag, MmGatekeeperID=MmGatekeeperID, MmH225Crv=MmH225Crv, MmErrorSeverity=MmErrorSeverity, mmH245Root=mmH245Root, mmH323GatewayRoot=mmH323GatewayRoot, MmAliasTag=MmAliasTag)
