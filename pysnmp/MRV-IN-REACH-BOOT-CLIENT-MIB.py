#
# PySNMP MIB module MRV-IN-REACH-BOOT-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MRV-IN-REACH-BOOT-CLIENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:05:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
mrvInReachProductDivision, = mibBuilder.importSymbols("MRV-IN-REACH-PRODUCT-DIVISION-MIB", "mrvInReachProductDivision")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Bits, Integer32, Gauge32, ModuleIdentity, iso, IpAddress, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, Counter64, MibIdentifier, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "Integer32", "Gauge32", "ModuleIdentity", "iso", "IpAddress", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "Counter64", "MibIdentifier", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
xBootClient = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 12))
bootClientStatus = MibScalar((1, 3, 6, 1, 4, 1, 33, 12, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 1400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bootClientStatus.setStatus('mandatory')
mibBuilder.exportSymbols("MRV-IN-REACH-BOOT-CLIENT-MIB", xBootClient=xBootClient, bootClientStatus=bootClientStatus)
