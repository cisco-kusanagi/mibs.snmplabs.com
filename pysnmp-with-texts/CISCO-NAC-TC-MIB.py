#
# PySNMP MIB module CISCO-NAC-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-NAC-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:51:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, IpAddress, MibIdentifier, ObjectIdentity, NotificationType, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, Gauge32, Integer32, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "MibIdentifier", "ObjectIdentity", "NotificationType", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "Gauge32", "Integer32", "TimeTicks", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoNacTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 530))
ciscoNacTcMIB.setRevisions(('2006-05-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoNacTcMIB.setRevisionsDescriptions(('The initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoNacTcMIB.setLastUpdated('200605310000Z')
if mibBuilder.loadTexts: ciscoNacTcMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoNacTcMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-nac@cisco.com cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoNacTcMIB.setDescription('This module defines the textual conventions for Cisco Network Admission Control(NAC) system. The Cisco Network Admission Control security solution offers a systems approach to customers for ensuring endpoint device compliancy and vulnerability checks prior to production access to the network. Cisco refers to these compliancy checks as posture validations. The intent of this systems approach is to prevent the spread of works, viruses, and rogue applications across the network. This systems approach requires integration with third party end point security applications, as well as endpoint security servers. Terminology used: EOU - Extensible Authentication Protocol over UDP. UCT - Un Conditional Transition. CTA - Cisco Trust Agent. EAP - Extensible Authentication Protocol. An extension to PPP. ACS/AAA - Cisco Secure Access Control Server. The primary authorization server that is the network policy decision point and is extended to support posture validation. NAD - Network Access Device that enforces network access control policies through layer 2 or layer 3 challenge-responses with a network enabled Endpoint device.')
class CnnEouState(TextualConvention, Integer32):
    description = "Describes the EOU state. initialize(1) Indicates that the EOU state is in initialization. State machine enters this state when a new IP has been learned on the port. Cleanup of the port configuration also force entering this state. When entering this state, the followings action take place: - any previously configured policy are removed - frees up any previously allocated memory - does a UCT to 'hello' state. hello(2) Indicates that the EOU state is in hello state. In this state the device sends a hello message to get the association ID of the CTA and also to check whether a CTA exists at all. The device starts the hello timer and waits till that time and if it doesn't get a response, it retransmits the hello requests for max-retry times before it declares the host as 'clientless'. clientless(3) Indicates that the EOU state is in client-less state. State machine enters this state when hello response is not reached and in this state the device does a pseudo authentication to download the policy for Non-Responsive hosts and stays in this state. eapRequest(4) Indicates that the EOU state is in EAP request state. In this state, the device sends EAP validate requests to the CTA and awaits response from the CTA, it starts the retransmit timeout and if response is not received before that timer expires, it retransmits the EAP requests. response(5) Indicates that the EOU state is in EAP response state. State machine enters this state when a response for the EAP validate request is received from the CTA. Device then builds a RADIUS request incorporating the EAP packet and sends it to the ACS and awaits response from the ACS. If the response from the ACS is an access challenge it moves the port the 'eapRequest' state. But if it's a success, port is moved to 'authenticated' state. If its Access- Reject, port is moved to 'fail' state. authenticated(6) Indicates that the EOU state is in authenticated state. In this state policy installation happens and port remains in this state until revalidation event is triggered because of session timer expiry or when status query fails. Status query generation and response reception happens in this state only. fail(7) Indicates that the EOU state is in failed state. When posture validation fails, system start the hold timer and device waits till it expires before trying for posture validation again. abort(8) Indicates that the EOU state is in abort state. State machine enters this state because of failing to complete posture validation due to lack of response from CTA/RADIUS or any other reason. aaaFail(9) Indicates that the EOU state is in AAA failed state. State machine enters this state when RADIUS requests to AAA server timeouts either due to the server not being reachable or is down. hold(10) Indicates that the EOU state is in hold state. This state represents the quiet or idle state for the host. The host is put in the hold state on events like hello response is not received or the AAA server is not reachable. Host remains in this state for hold the EOU hold timeout period. client(11) Indicates that the EOU state is in client state. This state is reached when the host sends a response to EOU hello request from the authenticating device. This state indicates the presence of CTA on the device. server(12) Indicates that the EOU state is in server state. This state represents that the authenticating device is communicating with the AAA (RADIUS) server. This state is reached when host send an EOU response."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("initialize", 1), ("hello", 2), ("clientless", 3), ("eapRequest", 4), ("response", 5), ("authenticated", 6), ("fail", 7), ("abort", 8), ("aaaFail", 9), ("hold", 10), ("client", 11), ("server", 12))

class CnnEouAuthType(TextualConvention, Integer32):
    description = 'Type of authentication for NAD. clientless(1) End point device that does not run Cisco Trust Agent. eap(2) Authorized via Extensible Authentication Protocol. static(3) Statically authorized or rejected individual end point device. unknown(4) The authentication type of the endpoint host is unknown.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("clientless", 1), ("eap", 2), ("static", 3), ("unknown", 4))

class CnnEouDeviceType(TextualConvention, Integer32):
    description = 'The supported exempt device type on NAD. ciscoIpPhone(1) - Cisco IP Phone'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("ciscoIpPhone", 1))

class CnnEouPostureToken(TextualConvention, Integer32):
    description = "Posture token which representing the endpoint device's relative compliance to the network compliance policy. unknown(1) The posture credentials of the endpoint host cannot be determined. The integrity of the endpoint should be determined so proper posture credentials can be attained and assessed for network access authorization. healthy(2) The host complies with the currently required credentials so no restrictions need to be placed on this device. checkup(3) The host is within policy but doesn't have the latest AV software; update recommended. This profile state may be used to signal management servers to proactively get this machine into the 'healthy' state. quarantine(4) The host is out of policy and needs to be restricted to a remediation network. This device is not actively placing a threat on other host but is susceptible to attack or infection and should be updated as soon as possible. infected(5) The host is an active threat to other hosts. Network access should be severely restricted and placed into remediation or totally denied all network access. This TEXTUAL-CONVENTION is deprecated and replaced by CnnEouPostureTokenString."
    status = 'deprecated'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 1), ("healthy", 2), ("checkup", 3), ("quarantine", 4), ("infected", 5))

class CnnEouPostureTokenString(TextualConvention, OctetString):
    description = "Posture token which representing the endpoint device's relative compliance to the network compliance policy. Valid characters are a-z, A-Z, 0-9, ,'#', '-', '_', and '.'. Posture token string is case sensitive and permits the value of empty string."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

mibBuilder.exportSymbols("CISCO-NAC-TC-MIB", CnnEouDeviceType=CnnEouDeviceType, PYSNMP_MODULE_ID=ciscoNacTcMIB, CnnEouAuthType=CnnEouAuthType, ciscoNacTcMIB=ciscoNacTcMIB, CnnEouState=CnnEouState, CnnEouPostureTokenString=CnnEouPostureTokenString, CnnEouPostureToken=CnnEouPostureToken)
