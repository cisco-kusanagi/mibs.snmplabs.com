#
# PySNMP MIB module FASTPATH-QOS-AUTOVOIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FASTPATH-QOS-AUTOVOIP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:12:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
fastPathQOS, = mibBuilder.importSymbols("FASTPATH-QOS-MIB", "fastPathQOS")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, IpAddress, ModuleIdentity, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, NotificationType, Gauge32, Unsigned32, MibIdentifier, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "ModuleIdentity", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "NotificationType", "Gauge32", "Unsigned32", "MibIdentifier", "Bits", "Counter64")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
fastPathQOSAUTOVOIP = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 4))
fastPathQOSAUTOVOIP.setRevisions(('2007-11-23 00:00', '2007-11-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fastPathQOSAUTOVOIP.setRevisionsDescriptions(('Broadcom branding related changes.', 'Initial revision.',))
if mibBuilder.loadTexts: fastPathQOSAUTOVOIP.setLastUpdated('200711230000Z')
if mibBuilder.loadTexts: fastPathQOSAUTOVOIP.setOrganization('Broadcom Corporation')
if mibBuilder.loadTexts: fastPathQOSAUTOVOIP.setContactInfo(' Customer Support Postal: Broadcom Corporation 100 Perimeter Park Drive Suite H Morrisville, NC 27560 Tel: +1 919 865 2700')
if mibBuilder.loadTexts: fastPathQOSAUTOVOIP.setDescription('The MIB definitions for Quality of Service - VoIP Flex package.')
class PercentByFives(TextualConvention, Unsigned32):
    description = 'An unsigned integer representing a value expressed as a percentage with five percent increments.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5, 5), ValueRangeConstraint(10, 10), ValueRangeConstraint(15, 15), ValueRangeConstraint(20, 20), ValueRangeConstraint(25, 25), ValueRangeConstraint(30, 30), ValueRangeConstraint(35, 35), ValueRangeConstraint(40, 40), ValueRangeConstraint(45, 45), ValueRangeConstraint(50, 50), ValueRangeConstraint(55, 55), ValueRangeConstraint(60, 60), ValueRangeConstraint(65, 65), ValueRangeConstraint(70, 70), ValueRangeConstraint(75, 75), ValueRangeConstraint(80, 80), ValueRangeConstraint(85, 85), ValueRangeConstraint(90, 90), ValueRangeConstraint(95, 95), ValueRangeConstraint(100, 100), )
class Sixteenths(TextualConvention, Unsigned32):
    description = 'An unsigned integer representing the numerator of a value expressing a fraction in terms of sixteenths (0/16, 1/16, 2/16, up to 16/16).'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16)

agentAutoVoIPCfgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 4, 1))
agentAutoVoIPTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 4, 1, 1), )
if mibBuilder.loadTexts: agentAutoVoIPTable.setStatus('current')
if mibBuilder.loadTexts: agentAutoVoIPTable.setDescription('A table providing configuration of Auto VoIP Profile.')
agentAutoVoIPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 4, 1, 1, 1), ).setIndexNames((0, "FASTPATH-QOS-AUTOVOIP-MIB", "agentAutoVoIPIntfIndex"))
if mibBuilder.loadTexts: agentAutoVoIPEntry.setStatus('current')
if mibBuilder.loadTexts: agentAutoVoIPEntry.setDescription('Auto VoIP Profile configuration for a port.')
agentAutoVoIPIntfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 4, 1, 1, 1, 1), InterfaceIndexOrZero())
if mibBuilder.loadTexts: agentAutoVoIPIntfIndex.setStatus('current')
if mibBuilder.loadTexts: agentAutoVoIPIntfIndex.setDescription('This is a unique index for an entry in the agentAutoVoIPTable. A non-zero value indicates the ifIndex for the corresponding interface entry in the ifTable. A value of zero represents global configuration, which in turn causes all interface entries to be updated for a set operation, or reflects the most recent global setting for a get operation.')
agentAutoVoIPMode = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 4, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentAutoVoIPMode.setStatus('current')
if mibBuilder.loadTexts: agentAutoVoIPMode.setDescription('Enables / disables AutoVoIP profile on an interface.')
agentAutoVoIPCosQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 4, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentAutoVoIPCosQueue.setStatus('current')
if mibBuilder.loadTexts: agentAutoVoIPCosQueue.setDescription('Cos Queue to which all VoIP traffic is mapped to.')
mibBuilder.exportSymbols("FASTPATH-QOS-AUTOVOIP-MIB", agentAutoVoIPTable=agentAutoVoIPTable, PercentByFives=PercentByFives, Sixteenths=Sixteenths, agentAutoVoIPIntfIndex=agentAutoVoIPIntfIndex, agentAutoVoIPMode=agentAutoVoIPMode, fastPathQOSAUTOVOIP=fastPathQOSAUTOVOIP, agentAutoVoIPEntry=agentAutoVoIPEntry, PYSNMP_MODULE_ID=fastPathQOSAUTOVOIP, agentAutoVoIPCosQueue=agentAutoVoIPCosQueue, agentAutoVoIPCfgGroup=agentAutoVoIPCfgGroup)
