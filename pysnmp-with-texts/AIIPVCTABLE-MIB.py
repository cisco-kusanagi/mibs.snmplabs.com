#
# PySNMP MIB module AIIPVCTABLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AIIPVCTABLE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:16:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, IpAddress, Counter32, ModuleIdentity, enterprises, iso, TimeTicks, Counter64, Gauge32, Integer32, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "IpAddress", "Counter32", "ModuleIdentity", "enterprises", "iso", "TimeTicks", "Counter64", "Gauge32", "Integer32", "Bits", "ObjectIdentity")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
class UnsignedShort(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class PositiveInteger(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class IfIndexType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

aii = MibIdentifier((1, 3, 6, 1, 4, 1, 539))
aiSLC2 = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 16))
aiPVC = ModuleIdentity((1, 3, 6, 1, 4, 1, 539, 16, 1))
if mibBuilder.loadTexts: aiPVC.setLastUpdated('9909141400Z')
if mibBuilder.loadTexts: aiPVC.setOrganization('Applied Innovation Inc.')
if mibBuilder.loadTexts: aiPVC.setContactInfo(' Engineering MIB Administrator Postal: Applied Innovation Inc. 5800 Innovation Drive Dublin, Ohio 43016-3271 Tel: 614-798-2000 Fax: 614-798-1770 E-mail: snmp@aiinet.com')
if mibBuilder.loadTexts: aiPVC.setDescription('The MIB module for the PVC Table')
class IANAifType(TextualConvention, Integer32):
    description = "This data type is used as the syntax of the ifType object in the (updated) definition of MIB-II's ifTable. The definition of this textual convention with the addition of newly assigned values is published periodically by the IANA, in either the Assigned Numbers RFC, or some derivative of it specific to Internet Network Management number assignments. (The latest arrangements can be obtained by contacting the IANA.) Requests for new values should be made to IANA via email (iana@isi.edu). The relationship between the assignment of ifType values and of OIDs to particular media-specific MIBs is solely the purview of IANA and is subject to change without notice. Quite often, a media-specific MIB's OID-subtree assignment within MIB-II's 'transmission' subtree will be the same as its ifType value. However, in some circumstances this will not be the case, and implementors must not pre-assume any specific relationship between ifType values and transmission subtree OIDs."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54))
    namedValues = NamedValues(("other", 1), ("regular1822", 2), ("hdh1822", 3), ("ddnX25", 4), ("rfc877x25", 5), ("ethernetCsmacd", 6), ("iso88023Csmacd", 7), ("iso88024TokenBus", 8), ("iso88025TokenRing", 9), ("iso88026Man", 10), ("starLan", 11), ("proteon10Mbit", 12), ("proteon80Mbit", 13), ("hyperchannel", 14), ("fddi", 15), ("lapb", 16), ("sdlc", 17), ("ds1", 18), ("e1", 19), ("basicISDN", 20), ("primaryISDN", 21), ("propPointToPointSerial", 22), ("ppp", 23), ("softwareLoopback", 24), ("eon", 25), ("ethernet3Mbit", 26), ("nsip", 27), ("slip", 28), ("ultra", 29), ("ds3", 30), ("sip", 31), ("frameRelay", 32), ("rs232", 33), ("para", 34), ("arcnet", 35), ("arcnetPlus", 36), ("atm", 37), ("miox25", 38), ("sonet", 39), ("x25ple", 40), ("iso88022llc", 41), ("localTalk", 42), ("smdsDxi", 43), ("frameRelayService", 44), ("v35", 45), ("hssi", 46), ("hippi", 47), ("modem", 48), ("aal5", 49), ("sonetPath", 50), ("sonetVT", 51), ("smdsIcip", 52), ("propVirtual", 53), ("propMultiplexor", 54))

aiPVCTable = MibTable((1, 3, 6, 1, 4, 1, 539, 16, 1, 1), )
if mibBuilder.loadTexts: aiPVCTable.setStatus('current')
if mibBuilder.loadTexts: aiPVCTable.setDescription(' Entries define permanent virtual circuits (PVCs) in the system. Each entry contains enough information to create one PVC on one network interface. Each entry may also contain the information required to create another circuit in the system, of any kind. This other circuit we will call a companion circuit, since eventually it is going to be connected to the PVC defined in the same entry. This connection information does not need to be present, but may be, to allow for a rapid association between a PVC and its companion circuit. ')
aiPVCEntry = MibTableRow((1, 3, 6, 1, 4, 1, 539, 16, 1, 1, 1), ).setIndexNames((0, "AIIPVCTABLE-MIB", "aiPVCIfType"), (0, "AIIPVCTABLE-MIB", "aiPVCIfIndex"), (0, "AIIPVCTABLE-MIB", "aiPVCCircuit"))
if mibBuilder.loadTexts: aiPVCEntry.setStatus('current')
if mibBuilder.loadTexts: aiPVCEntry.setDescription('Entries of aiPVCTable.')
aiPVCStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 1, 1, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aiPVCStatus.setStatus('current')
if mibBuilder.loadTexts: aiPVCStatus.setDescription(' The status of this PVC entry. See RFC 1443 for details of usage. ')
aiPVCIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 1, 1, 1, 2), IANAifType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiPVCIfType.setStatus('current')
if mibBuilder.loadTexts: aiPVCIfType.setDescription(' The type of subnetwork on which this PVC is to be created. Examples are frameRelay(32), and x25ple(40). ')
aiPVCIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 1, 1, 1, 3), IfIndexType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiPVCIfIndex.setStatus('current')
if mibBuilder.loadTexts: aiPVCIfIndex.setDescription(' The index into the interfaces group of MIB-II, which defines the particular subnetwork on which this PVC will be created. This index corresponds to what AII calls a link. ')
aiPVCCircuit = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 1, 1, 1, 4), PositiveInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiPVCCircuit.setStatus('current')
if mibBuilder.loadTexts: aiPVCCircuit.setDescription(' The individual circuit number on the subnetwork (defined by aiPVCIfIndex), to which the PVC defined by this entry is mapped. In X.25, this number maps directly to a Logical Channel Number. In Frame Relay, this number maps directly to a DLCI. In other words, this object, and aiPVCIfIndex, tell the SLC where a PVC is located. ')
aiPVCCallTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 1, 1, 1, 5), UnsignedShort()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiPVCCallTimer.setStatus('current')
if mibBuilder.loadTexts: aiPVCCallTimer.setDescription(' The time, in seconds, between successive attempts to create a composite circuit comprising the PVC defined in this entry, and its companion circuit. When a PVC is created, if its aiPVCCallTimer is greater than zero, then the PVC will attempt to connect to a remote host (as specified elsewhere). If the connection attempt times out before completion, then the PVC will try again after aiPVCCallTimer seconds. ')
aiPVCInactivityTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 1, 1, 1, 6), UnsignedShort()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiPVCInactivityTimer.setStatus('current')
if mibBuilder.loadTexts: aiPVCInactivityTimer.setDescription(" The time, in seconds, of inactivity on a composite circuit before a PVC will tear down the composite circuit. Once a composite circuit has been created, comprising a PVC and its companion circuit, then if the PVC's aiPVCInactivityTimer is greater than zero, and if no data passes through the composite circuit in either direction for aiPVCInactivityTimer seconds, then the PVC will close the composite circuit. ")
aiPVCConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 16, 1, 2))
aiPVCGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 16, 1, 2, 1))
aiPVCCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 16, 1, 2, 2))
aiPVCCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 539, 16, 1, 2, 2, 1)).setObjects(("AIIPVCTABLE-MIB", "aiPVCGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aiPVCCompliance = aiPVCCompliance.setStatus('current')
if mibBuilder.loadTexts: aiPVCCompliance.setDescription('The compliance statement for SNMPv2 entities which have AII PVC tables.')
aiPVCGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 539, 16, 1, 2, 1, 1)).setObjects(("AIIPVCTABLE-MIB", "aiPVCStatus"), ("AIIPVCTABLE-MIB", "aiPVCIfIndex"), ("AIIPVCTABLE-MIB", "aiPVCIfType"), ("AIIPVCTABLE-MIB", "aiPVCCircuit"), ("AIIPVCTABLE-MIB", "aiPVCCallTimer"), ("AIIPVCTABLE-MIB", "aiPVCInactivityTimer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aiPVCGroup = aiPVCGroup.setStatus('current')
if mibBuilder.loadTexts: aiPVCGroup.setDescription('A collection of objects providing information applicable to all AII cal parameter name tables.')
mibBuilder.exportSymbols("AIIPVCTABLE-MIB", aiPVCTable=aiPVCTable, IfIndexType=IfIndexType, IANAifType=IANAifType, aiPVCStatus=aiPVCStatus, aiPVCGroup=aiPVCGroup, aiPVCEntry=aiPVCEntry, PositiveInteger=PositiveInteger, aiPVCConformance=aiPVCConformance, aiSLC2=aiSLC2, PYSNMP_MODULE_ID=aiPVC, aiPVCIfType=aiPVCIfType, aiPVCGroups=aiPVCGroups, UnsignedShort=UnsignedShort, aiPVCCompliances=aiPVCCompliances, aiPVCCompliance=aiPVCCompliance, aiPVCInactivityTimer=aiPVCInactivityTimer, aiPVC=aiPVC, aiPVCCallTimer=aiPVCCallTimer, aiPVCIfIndex=aiPVCIfIndex, aii=aii, aiPVCCircuit=aiPVCCircuit)
