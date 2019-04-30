#
# PySNMP MIB module CXConsoleDriver-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXConsoleDriver-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:16:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
cxConsoleDriver, = mibBuilder.importSymbols("CXProduct-SMI", "cxConsoleDriver")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, TimeTicks, Gauge32, Counter32, Unsigned32, MibIdentifier, Bits, Counter64, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Gauge32", "Counter32", "Unsigned32", "MibIdentifier", "Bits", "Counter64", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cxCdBaudRate = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 6, 1), Integer32().clone(9600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCdBaudRate.setStatus('mandatory')
cxCdCharSize = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 6, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(7, 8)).clone(8)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCdCharSize.setStatus('mandatory')
cxCdParity = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 6, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noParity", 1), ("evenParity", 2), ("oddParity", 3))).clone('noParity')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCdParity.setStatus('mandatory')
cxCdStopBit = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 6, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCdStopBit.setStatus('mandatory')
cxCdProtocol = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 6, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("localConsole", 1), ("ppp", 2))).clone('localConsole')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCdProtocol.setStatus('mandatory')
mibBuilder.exportSymbols("CXConsoleDriver-MIB", cxCdProtocol=cxCdProtocol, cxCdStopBit=cxCdStopBit, cxCdCharSize=cxCdCharSize, cxCdParity=cxCdParity, cxCdBaudRate=cxCdBaudRate)
