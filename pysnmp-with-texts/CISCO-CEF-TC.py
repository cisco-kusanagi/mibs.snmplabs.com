#
# PySNMP MIB module CISCO-CEF-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CEF-TC
# Produced by pysmi-0.3.4 at Wed May  1 11:53:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, IpAddress, Counter32, MibIdentifier, Counter64, Unsigned32, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, ModuleIdentity, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "Counter32", "MibIdentifier", "Counter64", "Unsigned32", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "ModuleIdentity", "Bits", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCefTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 493))
ciscoCefTextualConventions.setRevisions(('2005-09-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCefTextualConventions.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCefTextualConventions.setLastUpdated('200509300000Z')
if mibBuilder.loadTexts: ciscoCefTextualConventions.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCefTextualConventions.setContactInfo('Postal: Cisco Systems, Inc. 170 West Tasman Drive San Jose, CA 95134-1706 USA Tel: +1 800 553-NETS E-mail: cs-cef@cisco.com')
if mibBuilder.loadTexts: ciscoCefTextualConventions.setDescription('This MIB module defines Textual Conventions and OBJECT-IDENTITIES for use in documents defining management information base (MIBs) modules for managing Cisco Express Forwarding (CEF).')
class CefIpVersion(TextualConvention, Integer32):
    description = 'The version of CEF IP forwarding.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2))

class CefAdjLinkType(TextualConvention, Integer32):
    description = 'Link type for the adjacency. The adjacency link type identifies protocol stack on neighbour device which will process packets fed through adjacency.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2), ("mpls", 3), ("raw", 4), ("unknown", 5))

class CefAdjacencySource(TextualConvention, Bits):
    description = "The mechanism by which the adjacency is learned. As the mechanism of learning the adjacency can be multiple (e.g. 'arp' and 'atmPVC'), hence the value of this object represents the bit mask of adjacency sources."
    status = 'current'
    namedValues = NamedValues(("atom", 0), ("linkRawAdj", 1), ("ipPseudowireAdj", 2), ("arp", 3), ("p2pAdj", 4), ("frMap", 5), ("atmPVC", 6), ("atmSVC", 7), ("atmTVC", 8), ("nbma", 9), ("mpoa", 10), ("atmBundle", 11), ("lec", 12), ("nhrp", 13), ("ipv6ND", 14), ("cmcc", 15), ("ipv6SixtoFourTunnel", 16), ("ipv6IsaTapTunnel", 17), ("ipv6AutoTunnel", 18), ("fibLc", 19), ("virtual", 20), ("multicast", 21), ("unknown", 22))

class CefPathType(TextualConvention, Integer32):
    description = 'Type of the CEF Path. receive(1) : path for the address configured on any of the interface in the device. connectedPrefix(2) : connected prefix path attachedPrefix(3) : attached prefix path attachedHost(4) : attached host path attachedNexthop(5) : attached next hop path recursiveNexthop(6) : recursive next hop path adjacencyPrefix(7) : adjacency prefix path specialPrefix(8) : special prefix path unknown(9): : unknown path .'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("receive", 1), ("connectedPrefix", 2), ("attachedPrefix", 3), ("attachedHost", 4), ("attachedNexthop", 5), ("recursiveNexthop", 6), ("adjacencyPrefix", 7), ("specialPrefix", 8), ("unknown", 9))

class CefPrefixSearchState(TextualConvention, Integer32):
    description = 'The state of prefix search operation. The description of each state is given below: running(1) : this state signifies that a prefix search request is running. matchFound(2) : this state signifies that a prefix search request is completed and a prefix match has been found. noMatchFound(3) : this state signifies that a prefix search request is completed and a prefix match has not been found. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("running", 1), ("matchFound", 2), ("noMatchFound", 3))

class CefForwardingElementSpecialType(TextualConvention, Integer32):
    description = 'Type of special forwarding element illegal(1) : illegal special forwarding element. the packet will be dropped. punt(2) : the packet will be punted to the next switching path drop(3) : not supported for Destination IP to next hop interface and the packet will be dropped discard(4) : the packet is for Destination IP through next hop interface and it will be discarded null(5) : the packet is for Destination IP to null0, it will be dropped glean(6) : an attempt will be made to complete the encapsulation string through address resolution unResolved(7): unresolved forwarding element. the packet will be dropped unconditionally. noRoute(8) : no route forwarding element. This forwarding element will result in rate limited punts to the next switching path(to generate ICMP no route message) none(9) : not a special forwarding element and the value of this object should be ignored '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("illegal", 1), ("punt", 2), ("drop", 3), ("discard", 4), ("null", 5), ("glean", 6), ("unresolved", 7), ("noRoute", 8), ("none", 9))

class CefMplsLabelList(TextualConvention, OctetString):
    description = "This contains a list of MPLS Labels, each separated by the ';' (semi-colon) character. MPLS Label values are in accordance with the MplsLabel TEXTUAL-CONVENTION defined in the MPLS-TC-MIB. The following is en example containing two MPLS labels: 4294;100 An empty string value for this object indicates no MPLS Labels in this list. "
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CefAdminStatus(TextualConvention, Integer32):
    description = 'Admin status of CEF. The admin status of CEF may differ from the oper status of CEF depending upon the success of the admin operation.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CefOperStatus(TextualConvention, Integer32):
    description = 'Operational status of CEF.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class CefFailureReason(TextualConvention, Integer32):
    description = 'Reason of CEF Failure: none(1) : no failure mallocFailure(2) : memory allocation failed for CEF hwFailure(3) : hardware interface failure for CEF keepaliveFailure(4) : keepalive was not received from the CEF peer entity noMsgBuffer(5) : message buffers were exhausted while preparing IPC message to be sent to the CEF peer entity invalidMsgSize(6) : IPC message was received with invalid size from the CEF peer entity internalError(7) : Some other internal error was detected for CEF '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("none", 1), ("mallocFailure", 2), ("hwFailure", 3), ("keepaliveFailure", 4), ("noMsgBuffer", 5), ("invalidMsgSize", 6), ("internalError", 7))

class CefCCType(TextualConvention, Integer32):
    description = 'Type of the consistency checker. lcDetect : This is an active consistency checker which is triggered when a packet cannot be forwarded because the prefix is not in the forwarding table. It Detects missing prefixes on the linecard CEF database by sending the missing prefixes to the RP. scanFibLcRp : This is an passive consistency checker which performs a passive scan check of the table on the line card. This consistency checker operates on the line card by examining the FIB table for a configurable time period and sending the next n prefixes to the RP. scanFibRpLc : This is an passive consistency checker which performs a passive scan check of RP by examining the FIB table for a configurable period and sending the next n prefixes to the line card. scanRibFib : This is an passive consistency checker which compares routing information base (RIB) to the FIB table at a configurable interval and provides the number of entries missing from the FIB table. scanFibRib : This is an passive consistency checker which compares FIB Tables to the routing information base (RIB) at a configurable interval and provides the number of entries missing from the FIB table. scanFibHwSw : This is an passive consistency checker which compares FIB Tables in hardware to the FIB Tables in RP. scanFibSwHw : This is an passive consistency checker which compares FIB Tables in RP to the FIB Tables in hardware. fullScanRibFib : This is an active consistency checker which is triggered by Management Station request. It compares the entire routing information base (RIB) to the FIB table and provide the number of entries missing from the FIB Table. fullScanFibRib : This is an active consistency checker which is triggered by Management Station request. It compares the FIB table to the routing information base (RIB) and provide the number of entries missing from the FIB Table. fullScanFibRpLc : This is an active consistency checker which is triggered by Management Station request. It compares the RP FIB Table with FIB Table on each LC and report inconsistencies. fullScanFibLcRp : This is an active consistency checker which is triggered by Management Station request. It compares the Fib Table on LC with FIB table on RP and report inconsistencies. fullScanFibHwSw : This is an active consistency checker which is triggered by Management Station request. It compares the Fib Table in hardware with FIB table in RP and report inconsistencies. fullScanFibSwHw : This is an active consistency checker which is triggered by Management Station request. It compares the Fib Table in RP with FIB table in hardware and report inconsistencies.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("lcDetect", 1), ("scanFibLcRp", 2), ("scanFibRpLc", 3), ("scanRibFib", 4), ("scanFibRib", 5), ("scanFibHwSw", 6), ("scanFibSwHw", 7), ("fullScanRibFib", 8), ("fullScanFibRib", 9), ("fullScanFibRpLc", 10), ("fullScanFibLcRp", 11), ("fullScanFibHwSw", 12), ("fullScanFibSwHw", 13))

class CefCCAction(TextualConvention, Integer32):
    description = 'The action to be performed for the consistency checkers. ccActionStart(1) : start the Consistency checker operation. ccActionAbort(2) : abort the Consistency checker operation. After aborting, the active process must recover. This can take some time, and during this period, the scan cannot be restarted. ccActionNone(3) : no operation is being performed on consistency checkers. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ccActionStart", 1), ("ccActionAbort", 2), ("ccActionNone", 3))

class CefCCStatus(TextualConvention, Integer32):
    description = 'The status of consistency checker operation. The description of each state is given below: ccStatusIdle(1) : this state signifies that no consistency checker request is being performed. ccStatusRunning(2) : this state signifies that consistency checker request is in progress. ccStatusDone(3) : this state signifies that consistency checker request is over. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ccStatusIdle", 1), ("ccStatusRunning", 2), ("ccStatusDone", 3))

mibBuilder.exportSymbols("CISCO-CEF-TC", CefAdjacencySource=CefAdjacencySource, CefMplsLabelList=CefMplsLabelList, CefOperStatus=CefOperStatus, CefCCType=CefCCType, CefForwardingElementSpecialType=CefForwardingElementSpecialType, ciscoCefTextualConventions=ciscoCefTextualConventions, CefCCAction=CefCCAction, CefAdjLinkType=CefAdjLinkType, CefFailureReason=CefFailureReason, CefIpVersion=CefIpVersion, CefCCStatus=CefCCStatus, CefPathType=CefPathType, PYSNMP_MODULE_ID=ciscoCefTextualConventions, CefPrefixSearchState=CefPrefixSearchState, CefAdminStatus=CefAdminStatus)
