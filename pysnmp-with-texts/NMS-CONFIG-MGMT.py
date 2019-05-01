#
# PySNMP MIB module NMS-CONFIG-MGMT (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMS-CONFIG-MGMT
# Produced by pysmi-0.3.4 at Wed May  1 14:21:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
nmsWorkGroup, = mibBuilder.importSymbols("NMS-SMI", "nmsWorkGroup")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Gauge32, ModuleIdentity, Integer32, ObjectIdentity, Counter64, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, NotificationType, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "ModuleIdentity", "Integer32", "ObjectIdentity", "Counter64", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "NotificationType", "Unsigned32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
linmsm = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 20, 15))
configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 20, 15, 1))
operation = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 20, 15, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: operation.setStatus('mandatory')
if mibBuilder.loadTexts: operation.setDescription('1 means to save the commmand configuration. 2 means to save ifIndex configuration.')
result = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 20, 15, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: result.setStatus('mandatory')
if mibBuilder.loadTexts: result.setDescription('')
mibBuilder.exportSymbols("NMS-CONFIG-MGMT", linmsm=linmsm, configuration=configuration, result=result, operation=operation)
