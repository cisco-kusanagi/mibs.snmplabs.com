#
# PySNMP MIB module CXOSP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXOSP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:17:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
cxOSP, = mibBuilder.importSymbols("CXProduct-SMI", "cxOSP")
AreaID, Validation = mibBuilder.importSymbols("RFC1253-MIB", "AreaID", "Validation")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, ModuleIdentity, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, Counter64, Counter32, iso, Unsigned32, Gauge32, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "Counter64", "Counter32", "iso", "Unsigned32", "Gauge32", "MibIdentifier", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ospAreaTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 43, 1), )
if mibBuilder.loadTexts: ospAreaTable.setStatus('mandatory')
ospAreaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 43, 1, 1), ).setIndexNames((0, "CXOSP-MIB", "ospAreaId"))
if mibBuilder.loadTexts: ospAreaEntry.setStatus('mandatory')
ospAreaId = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 43, 1, 1, 1), AreaID()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospAreaId.setStatus('mandatory')
ospAreaStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 43, 1, 1, 2), Validation().clone('valid')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospAreaStatus.setStatus('mandatory')
mibBuilder.exportSymbols("CXOSP-MIB", ospAreaId=ospAreaId, ospAreaTable=ospAreaTable, ospAreaStatus=ospAreaStatus, ospAreaEntry=ospAreaEntry)
