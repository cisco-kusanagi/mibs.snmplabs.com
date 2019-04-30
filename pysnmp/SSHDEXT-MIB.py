#
# PySNMP MIB module SSHDEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SSHDEXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:02:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
sshdExt, = mibBuilder.importSymbols("APENT-MIB", "sshdExt")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, ObjectIdentity, IpAddress, NotificationType, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, MibIdentifier, Integer32, ModuleIdentity, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "IpAddress", "NotificationType", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "MibIdentifier", "Integer32", "ModuleIdentity", "Unsigned32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
apSshdMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 43, 1))
if mibBuilder.loadTexts: apSshdMib.setLastUpdated('0004031500Z')
if mibBuilder.loadTexts: apSshdMib.setOrganization('ArrowPoint Communications Inc.')
apSshdKeepAlive = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 43, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSshdKeepAlive.setStatus('current')
apSshdKeyRegenerationInterval = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 43, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1440)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSshdKeyRegenerationInterval.setStatus('current')
apSshdPort = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 43, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(22, 65535)).clone(22)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSshdPort.setStatus('current')
apSshdServerKeyBits = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 43, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(512, 65535)).clone(768)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSshdServerKeyBits.setStatus('current')
mibBuilder.exportSymbols("SSHDEXT-MIB", PYSNMP_MODULE_ID=apSshdMib, apSshdMib=apSshdMib, apSshdKeepAlive=apSshdKeepAlive, apSshdServerKeyBits=apSshdServerKeyBits, apSshdKeyRegenerationInterval=apSshdKeyRegenerationInterval, apSshdPort=apSshdPort)
