#
# PySNMP MIB module UMSAGENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/UMSAGENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:21:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, Gauge32, Bits, Counter32, ObjectIdentity, IpAddress, MibIdentifier, NotificationType, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "Gauge32", "Bits", "Counter32", "ObjectIdentity", "IpAddress", "MibIdentifier", "NotificationType", "iso", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
Datetime, Sint32, Sint16, ibmpsgAgent, Uint16, Sint64, Real32, Sint8, Real64, Uint64, Boolean, Uint32, Uint8, String = mibBuilder.importSymbols("UMS-MIB", "Datetime", "Sint32", "Sint16", "ibmpsgAgent", "Uint16", "Sint64", "Real32", "Sint8", "Real64", "Uint64", "Boolean", "Uint32", "Uint8", "String")
iBMPSGHTTPConfigurationTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 10, 2), )
if mibBuilder.loadTexts: iBMPSGHTTPConfigurationTable.setStatus('mandatory')
iBMPSGHTTPConfigurationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 10, 2, 1), ).setIndexNames((0, "UMSAGENT-MIB", "iBMPSGHTTPConfigurationKeyIndex"))
if mibBuilder.loadTexts: iBMPSGHTTPConfigurationEntry.setStatus('mandatory')
iBMPSGHTTPConfigurationKeyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 10, 2, 1, 1), String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: iBMPSGHTTPConfigurationKeyIndex.setStatus('mandatory')
iBMPSGHTTPConfigurationSettingId = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 10, 2, 1, 2), String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: iBMPSGHTTPConfigurationSettingId.setStatus('mandatory')
iBMPSGHTTPConfigurationPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 10, 2, 1, 3), Uint16()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: iBMPSGHTTPConfigurationPort.setStatus('mandatory')
mibBuilder.exportSymbols("UMSAGENT-MIB", iBMPSGHTTPConfigurationEntry=iBMPSGHTTPConfigurationEntry, iBMPSGHTTPConfigurationKeyIndex=iBMPSGHTTPConfigurationKeyIndex, iBMPSGHTTPConfigurationPort=iBMPSGHTTPConfigurationPort, iBMPSGHTTPConfigurationSettingId=iBMPSGHTTPConfigurationSettingId, iBMPSGHTTPConfigurationTable=iBMPSGHTTPConfigurationTable)
