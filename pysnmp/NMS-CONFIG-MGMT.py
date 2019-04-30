#
# PySNMP MIB module NMS-CONFIG-MGMT (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMS-CONFIG-MGMT
# Produced by pysmi-0.3.4 at Mon Apr 29 20:11:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
nmsWorkGroup, = mibBuilder.importSymbols("NMS-SMI", "nmsWorkGroup")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, iso, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, NotificationType, Gauge32, ModuleIdentity, Counter64, Integer32, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "NotificationType", "Gauge32", "ModuleIdentity", "Counter64", "Integer32", "TimeTicks", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
linmsm = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 20, 15))
configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 20, 15, 1))
operation = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 20, 15, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: operation.setStatus('mandatory')
result = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 20, 15, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: result.setStatus('mandatory')
mibBuilder.exportSymbols("NMS-CONFIG-MGMT", configuration=configuration, linmsm=linmsm, operation=operation, result=result)
