#
# PySNMP MIB module XYLAN-ATMLSM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYLAN-ATMLSM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:44:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, MibIdentifier, NotificationType, Unsigned32, ObjectIdentity, Integer32, ModuleIdentity, Counter32, Gauge32, TimeTicks, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "MibIdentifier", "NotificationType", "Unsigned32", "ObjectIdentity", "Integer32", "ModuleIdentity", "Counter32", "Gauge32", "TimeTicks", "Counter64", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
atmxLsmGroup, = mibBuilder.importSymbols("XYLAN-ATM-MIB", "atmxLsmGroup")
class AtmForumLaneAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(20, 20)
    fixedLength = 20

atmxLesConfTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 4, 13, 1), )
if mibBuilder.loadTexts: atmxLesConfTable.setStatus('mandatory')
if mibBuilder.loadTexts: atmxLesConfTable.setDescription('This table contains all the configuration parameters for a LAN Emulation client. ')
atmxLesConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 4, 13, 1, 1), ).setIndexNames((0, "XYLAN-ATMLSM-MIB", "atmxlesConfIndex"))
if mibBuilder.loadTexts: atmxLesConfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: atmxLesConfEntry.setDescription('Each table entry contains configuration information for one LAN Emulation Client. Most of the objects are derived from Initial State Parameters in the LAN Emulation specification.')
atmxlesConfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 13, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: atmxlesConfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: atmxlesConfIndex.setDescription('A value which uniquely identifies a conceptual row in the lesConfTable. If the conceptual row identified by this value of lesConfIndex is recreated following an agent restart, the same value of lesConfIndex must be used to identify the recreated row.')
atmxLesRedundancyEnabled = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 4, 13, 1, 1, 19), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxLesRedundancyEnabled.setStatus('mandatory')
if mibBuilder.loadTexts: atmxLesRedundancyEnabled.setDescription('This is to enable or disable redundency. 1 = ENABLE 2 = DISABLE')
atmxLesRedundancyRole = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 13, 1, 1, 20), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxLesRedundancyRole.setStatus('mandatory')
if mibBuilder.loadTexts: atmxLesRedundancyRole.setDescription('This is to specify redundency. 1 = Primary 2 = Secondary')
atmxSecondaryLESAtmAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 13, 1, 1, 21), AtmForumLaneAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxSecondaryLESAtmAddr.setStatus('mandatory')
if mibBuilder.loadTexts: atmxSecondaryLESAtmAddr.setDescription("This is to specify the secondary LES' Atm Address. It is valid only if atmxLesRedundancyRole = 2.")
mibBuilder.exportSymbols("XYLAN-ATMLSM-MIB", atmxLesRedundancyRole=atmxLesRedundancyRole, atmxLesConfTable=atmxLesConfTable, atmxLesRedundancyEnabled=atmxLesRedundancyEnabled, atmxSecondaryLESAtmAddr=atmxSecondaryLESAtmAddr, atmxLesConfEntry=atmxLesConfEntry, atmxlesConfIndex=atmxlesConfIndex, AtmForumLaneAddress=AtmForumLaneAddress)
