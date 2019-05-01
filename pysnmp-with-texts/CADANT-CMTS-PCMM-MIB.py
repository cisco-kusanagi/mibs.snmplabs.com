#
# PySNMP MIB module CADANT-CMTS-PCMM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CADANT-CMTS-PCMM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:45:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
cadPCMibObjects, = mibBuilder.importSymbols("CADANT-CMTS-PACKETCABLE-MIB", "cadPCMibObjects")
AdminState, = mibBuilder.importSymbols("CADANT-TC", "AdminState")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, NotificationType, Bits, TimeTicks, Gauge32, Unsigned32, ModuleIdentity, MibIdentifier, iso, ObjectIdentity, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "NotificationType", "Bits", "TimeTicks", "Gauge32", "Unsigned32", "ModuleIdentity", "MibIdentifier", "iso", "ObjectIdentity", "Integer32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cadPCMMMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 3))
cadPCMMMib.setRevisions(('2010-06-01 00:00', '2009-10-19 00:00', '2009-09-21 00:00', '2005-03-11 00:00', '2004-05-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cadPCMMMib.setRevisionsDescriptions(('Add cadPCMMSubscriberIdVrfName.', 'Add CopsVersion I05.', 'Add CopsVersion.', 'Modify the unit of cadPCMMTimerT1 to deciseconds.', 'v1.0 - Original version',))
if mibBuilder.loadTexts: cadPCMMMib.setLastUpdated('201006010000Z')
if mibBuilder.loadTexts: cadPCMMMib.setOrganization('Arris')
if mibBuilder.loadTexts: cadPCMMMib.setContactInfo('Arris Suite 180 2400 E. Ogden Avenue Lisle, IL 60532 U.S.A.')
if mibBuilder.loadTexts: cadPCMMMib.setDescription('This MIB Module supplies the management objects which are specific to the PacketCable Multimedia client of COPS. The objects for the management of the standard COPS protocol reside in RFC2940.')
class CopsVersion(TextualConvention, Integer32):
    description = 'This TEXTUAL-CONVENTION describes the major PCMM COPS releases available on the C4.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("i02", 1), ("i03", 2), ("i04", 3), ("i05", 4))

cadPCMMMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 3, 1))
cadPCMMConfigBase = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 3, 1, 1))
cadPCMMAdminState = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 3, 1, 1, 1), AdminState().clone('down')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadPCMMAdminState.setStatus('current')
if mibBuilder.loadTexts: cadPCMMAdminState.setDescription('The administrative state of PacketCable Multimedia services on the CMTS.')
cadPCMMTimerT1 = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 3, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 3000)).clone(300)).setUnits('deciseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadPCMMTimerT1.setStatus('current')
if mibBuilder.loadTexts: cadPCMMTimerT1.setDescription('Timer T1 limits the amount of time the Gate authorization remains valid without a resource reservaton.')
cadPCMMCopsVersion = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 3, 1, 1, 3), CopsVersion().clone('i05')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadPCMMCopsVersion.setStatus('current')
if mibBuilder.loadTexts: cadPCMMCopsVersion.setDescription('This object describes the PCMM COPS version that the C4 will advertise in the OPN message.')
cadPCMMSubscriberIdVrfName = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 3, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadPCMMSubscriberIdVrfName.setStatus('current')
if mibBuilder.loadTexts: cadPCMMSubscriberIdVrfName.setDescription('The name of the virtual router (VRF) that will be used to determine where a subscriberID remotely connected is located. If the specified VRF does not exist, then the default VRF will be used instead.')
mibBuilder.exportSymbols("CADANT-CMTS-PCMM-MIB", cadPCMMSubscriberIdVrfName=cadPCMMSubscriberIdVrfName, CopsVersion=CopsVersion, cadPCMMCopsVersion=cadPCMMCopsVersion, PYSNMP_MODULE_ID=cadPCMMMib, cadPCMMMibObjects=cadPCMMMibObjects, cadPCMMConfigBase=cadPCMMConfigBase, cadPCMMMib=cadPCMMMib, cadPCMMTimerT1=cadPCMMTimerT1, cadPCMMAdminState=cadPCMMAdminState)
