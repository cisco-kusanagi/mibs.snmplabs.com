#
# PySNMP MIB module TPLINK-ETHERNETOAMRFICFG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-ETHERNETOAMRFICFG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:17:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Integer32, TimeTicks, Counter64, ObjectIdentity, ModuleIdentity, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, Unsigned32, IpAddress, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "TimeTicks", "Counter64", "ObjectIdentity", "ModuleIdentity", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "Unsigned32", "IpAddress", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ethernetOamRfiConfig, = mibBuilder.importSymbols("TPLINK-ETHERNETOAM-MIB", "ethernetOamRfiConfig")
ethernetOamRfiCfgTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 3, 1), )
if mibBuilder.loadTexts: ethernetOamRfiCfgTable.setStatus('current')
ethernetOamRfiCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ethernetOamRfiCfgEntry.setStatus('current')
ethernetOamRfiCfgPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 3, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamRfiCfgPort.setStatus('current')
ethernetOamRfiCfgDyingGaspNotify = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetOamRfiCfgDyingGaspNotify.setStatus('current')
ethernetOamRfiCfgCriticalEventNotify = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetOamRfiCfgCriticalEventNotify.setStatus('current')
ethernetOamRfiCfgLAG = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 3, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamRfiCfgLAG.setStatus('current')
mibBuilder.exportSymbols("TPLINK-ETHERNETOAMRFICFG-MIB", ethernetOamRfiCfgDyingGaspNotify=ethernetOamRfiCfgDyingGaspNotify, ethernetOamRfiCfgPort=ethernetOamRfiCfgPort, ethernetOamRfiCfgTable=ethernetOamRfiCfgTable, ethernetOamRfiCfgLAG=ethernetOamRfiCfgLAG, ethernetOamRfiCfgCriticalEventNotify=ethernetOamRfiCfgCriticalEventNotify, ethernetOamRfiCfgEntry=ethernetOamRfiCfgEntry)
