#
# PySNMP MIB module CADANT-CMTS-PCMM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CADANT-CMTS-PCMM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:27:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
cadPCMibObjects, = mibBuilder.importSymbols("CADANT-CMTS-PACKETCABLE-MIB", "cadPCMibObjects")
AdminState, = mibBuilder.importSymbols("CADANT-TC", "AdminState")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, TimeTicks, Counter64, Integer32, NotificationType, Gauge32, Unsigned32, IpAddress, ModuleIdentity, Counter32, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "TimeTicks", "Counter64", "Integer32", "NotificationType", "Gauge32", "Unsigned32", "IpAddress", "ModuleIdentity", "Counter32", "MibIdentifier", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cadPCMMMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 3))
cadPCMMMib.setRevisions(('2010-06-01 00:00', '2009-10-19 00:00', '2009-09-21 00:00', '2005-03-11 00:00', '2004-05-05 00:00',))
if mibBuilder.loadTexts: cadPCMMMib.setLastUpdated('201006010000Z')
if mibBuilder.loadTexts: cadPCMMMib.setOrganization('Arris')
class CopsVersion(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("i02", 1), ("i03", 2), ("i04", 3), ("i05", 4))

cadPCMMMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 3, 1))
cadPCMMConfigBase = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 3, 1, 1))
cadPCMMAdminState = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 3, 1, 1, 1), AdminState().clone('down')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadPCMMAdminState.setStatus('current')
cadPCMMTimerT1 = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 3, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 3000)).clone(300)).setUnits('deciseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadPCMMTimerT1.setStatus('current')
cadPCMMCopsVersion = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 3, 1, 1, 3), CopsVersion().clone('i05')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadPCMMCopsVersion.setStatus('current')
cadPCMMSubscriberIdVrfName = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 3, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadPCMMSubscriberIdVrfName.setStatus('current')
mibBuilder.exportSymbols("CADANT-CMTS-PCMM-MIB", cadPCMMSubscriberIdVrfName=cadPCMMSubscriberIdVrfName, cadPCMMConfigBase=cadPCMMConfigBase, CopsVersion=CopsVersion, cadPCMMTimerT1=cadPCMMTimerT1, cadPCMMAdminState=cadPCMMAdminState, cadPCMMMib=cadPCMMMib, PYSNMP_MODULE_ID=cadPCMMMib, cadPCMMCopsVersion=cadPCMMCopsVersion, cadPCMMMibObjects=cadPCMMMibObjects)
