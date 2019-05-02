#
# PySNMP MIB module TPLINK-ETHERNETOAMRFICFG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-ETHERNETOAMRFICFG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:24:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, IpAddress, Unsigned32, Counter64, Gauge32, ObjectIdentity, iso, NotificationType, MibIdentifier, Counter32, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "IpAddress", "Unsigned32", "Counter64", "Gauge32", "ObjectIdentity", "iso", "NotificationType", "MibIdentifier", "Counter32", "Bits", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ethernetOamRfiConfig, = mibBuilder.importSymbols("TPLINK-ETHERNETOAM-MIB", "ethernetOamRfiConfig")
ethernetOamRfiCfgTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 3, 1), )
if mibBuilder.loadTexts: ethernetOamRfiCfgTable.setStatus('current')
if mibBuilder.loadTexts: ethernetOamRfiCfgTable.setDescription('A table that contains remote failure indication configuration of each port. Ethernet faults are difficult to diagnose, especially when physical communication is still maintained but network performance is decreasing gradually. OAMPDU defines a flag to allow an OAM entity to send information to the peer. The flag defines an emergency link event supported by OAM.')
ethernetOamRfiCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ethernetOamRfiCfgEntry.setStatus('current')
if mibBuilder.loadTexts: ethernetOamRfiCfgEntry.setDescription('An entry that contains the remote failure indication configuration of each port.')
ethernetOamRfiCfgPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 3, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamRfiCfgPort.setStatus('current')
if mibBuilder.loadTexts: ethernetOamRfiCfgPort.setDescription('Displays the port number.')
ethernetOamRfiCfgDyingGaspNotify = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetOamRfiCfgDyingGaspNotify.setStatus('current')
if mibBuilder.loadTexts: ethernetOamRfiCfgDyingGaspNotify.setDescription('Select to enable or disable the event notification when critical link event is Dying Gasp.')
ethernetOamRfiCfgCriticalEventNotify = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetOamRfiCfgCriticalEventNotify.setStatus('current')
if mibBuilder.loadTexts: ethernetOamRfiCfgCriticalEventNotify.setDescription('Select to enable or disable the event notification when critical link event is Critical Event.')
ethernetOamRfiCfgLAG = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 3, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamRfiCfgLAG.setStatus('current')
if mibBuilder.loadTexts: ethernetOamRfiCfgLAG.setDescription('Displays the LAG number of the port.')
mibBuilder.exportSymbols("TPLINK-ETHERNETOAMRFICFG-MIB", ethernetOamRfiCfgDyingGaspNotify=ethernetOamRfiCfgDyingGaspNotify, ethernetOamRfiCfgCriticalEventNotify=ethernetOamRfiCfgCriticalEventNotify, ethernetOamRfiCfgTable=ethernetOamRfiCfgTable, ethernetOamRfiCfgPort=ethernetOamRfiCfgPort, ethernetOamRfiCfgEntry=ethernetOamRfiCfgEntry, ethernetOamRfiCfgLAG=ethernetOamRfiCfgLAG)
