#
# PySNMP MIB module NMS-EPON-ONU-REMOTE-SERVER-INFO (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMS-EPON-ONU-REMOTE-SERVER-INFO
# Produced by pysmi-0.3.4 at Mon Apr 29 20:12:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
nmsEPONGroup, = mibBuilder.importSymbols("NMS-SMI", "nmsEPONGroup")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, iso, Gauge32, MibIdentifier, Counter32, ModuleIdentity, NotificationType, IpAddress, Integer32, ObjectIdentity, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "Gauge32", "MibIdentifier", "Counter32", "ModuleIdentity", "NotificationType", "IpAddress", "Integer32", "ObjectIdentity", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
nmsEponOnuRemoteServer = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 101, 28))
nmsEponOnuRemoteServerTable = MibTable((1, 3, 6, 1, 4, 1, 11606, 10, 101, 28, 1), )
if mibBuilder.loadTexts: nmsEponOnuRemoteServerTable.setStatus('mandatory')
nmsEponOnuRemoteServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11606, 10, 101, 28, 1, 1), ).setIndexNames((0, "NMS-EPON-ONU-REMOTE-SERVER-INFO", "onuRemoteServerIndex"))
if mibBuilder.loadTexts: nmsEponOnuRemoteServerEntry.setStatus('mandatory')
onuRemoteServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 28, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: onuRemoteServerIndex.setStatus('mandatory')
onuRemoteServerIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 28, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: onuRemoteServerIpAddr.setStatus('mandatory')
onuRemoteServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 28, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: onuRemoteServerRowStatus.setStatus('mandatory')
mibBuilder.exportSymbols("NMS-EPON-ONU-REMOTE-SERVER-INFO", nmsEponOnuRemoteServer=nmsEponOnuRemoteServer, onuRemoteServerRowStatus=onuRemoteServerRowStatus, nmsEponOnuRemoteServerEntry=nmsEponOnuRemoteServerEntry, nmsEponOnuRemoteServerTable=nmsEponOnuRemoteServerTable, onuRemoteServerIndex=onuRemoteServerIndex, onuRemoteServerIpAddr=onuRemoteServerIpAddr)
