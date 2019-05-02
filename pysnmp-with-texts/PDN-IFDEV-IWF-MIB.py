#
# PySNMP MIB module PDN-IFDEV-IWF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-IFDEV-IWF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:38:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
pdn_interfaces, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-interfaces")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Unsigned32, TimeTicks, Counter32, iso, NotificationType, IpAddress, Gauge32, Integer32, ObjectIdentity, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "TimeTicks", "Counter32", "iso", "NotificationType", "IpAddress", "Gauge32", "Integer32", "ObjectIdentity", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pdnIfDevIwfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27))
pdnIfDevIwfMIB.setRevisions(('2004-09-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pdnIfDevIwfMIB.setRevisionsDescriptions(('Initial release.',))
if mibBuilder.loadTexts: pdnIfDevIwfMIB.setLastUpdated('200409100000Z')
if mibBuilder.loadTexts: pdnIfDevIwfMIB.setOrganization('Paradyne Networks MIB Working Group Other information about group editing the MIB')
if mibBuilder.loadTexts: pdnIfDevIwfMIB.setContactInfo('Paradyne Networks, Inc. 8545 126th Avenue North Largo, FL 33733 www.paradyne.com General Comments to: mibwg_team@paradyne.com Editor Clay Sikes')
if mibBuilder.loadTexts: pdnIfDevIwfMIB.setDescription("This module provides objects pertaining to the management of an `Interface Device Interworking Function' (IfDev IWF). The following documents should be referenced with respect to this MIB module: [RFC 1662] Simpson, W., `PPP in HDLC-like framing', July 1994.")
pdnIfDevIwfNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 0))
pdnIfDevIwfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 1))
pdnIfDevIwfAFNs = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 2))
pdnIfDevIwfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3))
class TxRxUnit(TextualConvention, Integer32):
    reference = "RFC 1662, Section 1.2, `Terminology'."
    description = 'Identifies the unit of transmission. The unit other(1) is used when none of the other enumerations apply. The unit bits(2) is used when bits are being transmitted. The unit octets(3) is used for groups of 8 bits. The unit frames(4) is used for transmission at the data link layer. A frame may include a header and/or a trailer, along with some number of units of data. The unit packets(5) is a basic unit of encapsulation, which typically is passed across the interface between the network layer and the data link layer. A packet is usually mapped to a frame; the exceptions are when data link layer fragmentation is being performed, or when multiple packets are incorporated into a single frame. The unit datagrams(6) is a unit of transmission in the network layer (such as IP). A datagram may be encapsulated in one or more packets passed to the data link layer.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("bits", 2), ("octets", 3), ("frames", 4), ("packets", 5), ("datagrams", 6))

pdnIfDevIwfStatsTotalTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 1, 1), )
if mibBuilder.loadTexts: pdnIfDevIwfStatsTotalTable.setStatus('current')
if mibBuilder.loadTexts: pdnIfDevIwfStatsTotalTable.setDescription("The IfDev IWF Total Statistics Table. This table contains counters for statistics. Counters in this group contain `total' counts which are marked from the time the system was last re-initialized.")
pdnIfDevIwfStatsTotalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pdnIfDevIwfStatsTotalEntry.setStatus('current')
if mibBuilder.loadTexts: pdnIfDevIwfStatsTotalEntry.setDescription('An entry in the IfDev IWF Total Statistics Table.')
pdnIfDevIwfStatsTotalBufferUnderruns = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnIfDevIwfStatsTotalBufferUnderruns.setStatus('current')
if mibBuilder.loadTexts: pdnIfDevIwfStatsTotalBufferUnderruns.setDescription('The number of times there was a buffer underrun.')
pdnIfDevIwfStatsTotalMRUErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnIfDevIwfStatsTotalMRUErrors.setStatus('current')
if mibBuilder.loadTexts: pdnIfDevIwfStatsTotalMRUErrors.setDescription('The number of times the Maximum Receive Unit size was exceeded.')
pdnIfDevIwfStatsTotalRxUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 1, 1, 1, 3), TxRxUnit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnIfDevIwfStatsTotalRxUnit.setStatus('current')
if mibBuilder.loadTexts: pdnIfDevIwfStatsTotalRxUnit.setDescription('The unit type of data being received by the IWF.')
pdnIfDevIwfStatsTotalRx = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnIfDevIwfStatsTotalRx.setStatus('current')
if mibBuilder.loadTexts: pdnIfDevIwfStatsTotalRx.setDescription('The number of units received by the IWF.')
pdnIfDevIwfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 1))
pdnIfDevIwfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 2))
pdnIfDevIwfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 1, 1)).setObjects(("PDN-IFDEV-IWF-MIB", "pdnIfDevIwfStatsTotalBufferUnderrunsGroup"), ("PDN-IFDEV-IWF-MIB", "pdnIfDevIwfStatsTotalMRUErrorsGroup"), ("PDN-IFDEV-IWF-MIB", "pdnIfDevIwfStatsTotalRxGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnIfDevIwfCompliance = pdnIfDevIwfCompliance.setStatus('current')
if mibBuilder.loadTexts: pdnIfDevIwfCompliance.setDescription('The compliance statement for IfDev IWFs.')
pdnIfDevIwfObjGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 2, 1))
pdnIfDevIwfAfnGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 2, 2))
pdnIfDevIwfNtfyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 2, 3))
pdnIfDevIwfStatsTotalBufferUnderrunsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 2, 1, 1)).setObjects(("PDN-IFDEV-IWF-MIB", "pdnIfDevIwfStatsTotalBufferUnderruns"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnIfDevIwfStatsTotalBufferUnderrunsGroup = pdnIfDevIwfStatsTotalBufferUnderrunsGroup.setStatus('current')
if mibBuilder.loadTexts: pdnIfDevIwfStatsTotalBufferUnderrunsGroup.setDescription('The number of times there was a buffer underrun.')
pdnIfDevIwfStatsTotalMRUErrorsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 2, 1, 2)).setObjects(("PDN-IFDEV-IWF-MIB", "pdnIfDevIwfStatsTotalMRUErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnIfDevIwfStatsTotalMRUErrorsGroup = pdnIfDevIwfStatsTotalMRUErrorsGroup.setStatus('current')
if mibBuilder.loadTexts: pdnIfDevIwfStatsTotalMRUErrorsGroup.setDescription('The number of times the Maximum Receive Unit size was exceeded.')
pdnIfDevIwfStatsTotalRxGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 2, 1, 3)).setObjects(("PDN-IFDEV-IWF-MIB", "pdnIfDevIwfStatsTotalRxUnit"), ("PDN-IFDEV-IWF-MIB", "pdnIfDevIwfStatsTotalRx"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnIfDevIwfStatsTotalRxGroup = pdnIfDevIwfStatsTotalRxGroup.setStatus('current')
if mibBuilder.loadTexts: pdnIfDevIwfStatsTotalRxGroup.setDescription('The number of units received by the IWF.')
mibBuilder.exportSymbols("PDN-IFDEV-IWF-MIB", pdnIfDevIwfConformance=pdnIfDevIwfConformance, pdnIfDevIwfNtfyGroups=pdnIfDevIwfNtfyGroups, pdnIfDevIwfStatsTotalBufferUnderruns=pdnIfDevIwfStatsTotalBufferUnderruns, pdnIfDevIwfCompliance=pdnIfDevIwfCompliance, pdnIfDevIwfStatsTotalMRUErrorsGroup=pdnIfDevIwfStatsTotalMRUErrorsGroup, pdnIfDevIwfNotifications=pdnIfDevIwfNotifications, pdnIfDevIwfObjects=pdnIfDevIwfObjects, pdnIfDevIwfAFNs=pdnIfDevIwfAFNs, pdnIfDevIwfStatsTotalRxUnit=pdnIfDevIwfStatsTotalRxUnit, pdnIfDevIwfStatsTotalBufferUnderrunsGroup=pdnIfDevIwfStatsTotalBufferUnderrunsGroup, TxRxUnit=TxRxUnit, pdnIfDevIwfStatsTotalMRUErrors=pdnIfDevIwfStatsTotalMRUErrors, pdnIfDevIwfStatsTotalRx=pdnIfDevIwfStatsTotalRx, pdnIfDevIwfStatsTotalRxGroup=pdnIfDevIwfStatsTotalRxGroup, pdnIfDevIwfGroups=pdnIfDevIwfGroups, PYSNMP_MODULE_ID=pdnIfDevIwfMIB, pdnIfDevIwfStatsTotalTable=pdnIfDevIwfStatsTotalTable, pdnIfDevIwfStatsTotalEntry=pdnIfDevIwfStatsTotalEntry, pdnIfDevIwfAfnGroups=pdnIfDevIwfAfnGroups, pdnIfDevIwfCompliances=pdnIfDevIwfCompliances, pdnIfDevIwfMIB=pdnIfDevIwfMIB, pdnIfDevIwfObjGroups=pdnIfDevIwfObjGroups)
