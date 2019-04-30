#
# PySNMP MIB module CXSmae-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXSmae-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:17:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
cxSystemManagement, = mibBuilder.importSymbols("CXProduct-SMI", "cxSystemManagement")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, TimeTicks, Integer32, IpAddress, Counter32, Unsigned32, Bits, MibIdentifier, NotificationType, ModuleIdentity, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "Integer32", "IpAddress", "Counter32", "Unsigned32", "Bits", "MibIdentifier", "NotificationType", "ModuleIdentity", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cxSmRestart = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 13, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("system-idle", 0), ("warm-start-save-end", 1), ("cold-start", 2), ("warm-start-without-save", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxSmRestart.setStatus('mandatory')
cxSmConfig = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 13, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("save", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: cxSmConfig.setStatus('mandatory')
mibBuilder.exportSymbols("CXSmae-MIB", cxSmRestart=cxSmRestart, cxSmConfig=cxSmConfig)
