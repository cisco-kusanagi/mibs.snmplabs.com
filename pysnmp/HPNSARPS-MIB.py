#
# PySNMP MIB module HPNSARPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPNSARPS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:30:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Bits, NotificationType, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, IpAddress, ObjectIdentity, Integer32, enterprises, Counter64, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "NotificationType", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "IpAddress", "ObjectIdentity", "Integer32", "enterprises", "Counter64", "Gauge32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hp = MibIdentifier((1, 3, 6, 1, 4, 1, 11))
nm = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2))
hpnsa = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23))
hpnsaRPS = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 22))
hpnsaRPSMibRev = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 22, 1))
hpnsaRPSMibRevMajor = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 22, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaRPSMibRevMajor.setStatus('mandatory')
hpnsaRPSMibRevMinor = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 22, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaRPSMibRevMinor.setStatus('mandatory')
mibBuilder.exportSymbols("HPNSARPS-MIB", hp=hp, hpnsaRPSMibRev=hpnsaRPSMibRev, hpnsaRPSMibRevMinor=hpnsaRPSMibRevMinor, hpnsa=hpnsa, hpnsaRPSMibRevMajor=hpnsaRPSMibRevMajor, nm=nm, hpnsaRPS=hpnsaRPS)
