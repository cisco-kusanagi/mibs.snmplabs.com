#
# PySNMP MIB module MRV-IN-REACH-BOOT-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MRV-IN-REACH-BOOT-CLIENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:15:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
mrvInReachProductDivision, = mibBuilder.importSymbols("MRV-IN-REACH-PRODUCT-DIVISION-MIB", "mrvInReachProductDivision")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, NotificationType, ObjectIdentity, Unsigned32, Bits, ModuleIdentity, IpAddress, iso, Counter32, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "ModuleIdentity", "IpAddress", "iso", "Counter32", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
xBootClient = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 12))
bootClientStatus = MibScalar((1, 3, 6, 1, 4, 1, 33, 12, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 1400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bootClientStatus.setStatus('mandatory')
if mibBuilder.loadTexts: bootClientStatus.setDescription('The overall status of the bootstrapping operation, including, for example, what is presently happening and error information.')
mibBuilder.exportSymbols("MRV-IN-REACH-BOOT-CLIENT-MIB", xBootClient=xBootClient, bootClientStatus=bootClientStatus)
