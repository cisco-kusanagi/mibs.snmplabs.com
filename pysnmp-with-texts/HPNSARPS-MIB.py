#
# PySNMP MIB module HPNSARPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPNSARPS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:42:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, MibIdentifier, Integer32, Counter64, IpAddress, Unsigned32, Counter32, ObjectIdentity, NotificationType, ModuleIdentity, iso, Bits, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "MibIdentifier", "Integer32", "Counter64", "IpAddress", "Unsigned32", "Counter32", "ObjectIdentity", "NotificationType", "ModuleIdentity", "iso", "Bits", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hp = MibIdentifier((1, 3, 6, 1, 4, 1, 11))
nm = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2))
hpnsa = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23))
hpnsaRPS = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 22))
hpnsaRPSMibRev = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 22, 1))
hpnsaRPSMibRevMajor = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 22, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaRPSMibRevMajor.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaRPSMibRevMajor.setDescription('The major revision level of the MIB.')
hpnsaRPSMibRevMinor = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 22, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaRPSMibRevMinor.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaRPSMibRevMinor.setDescription('The minor revision level of the MIB.')
mibBuilder.exportSymbols("HPNSARPS-MIB", hpnsaRPSMibRev=hpnsaRPSMibRev, hpnsaRPSMibRevMajor=hpnsaRPSMibRevMajor, hp=hp, hpnsaRPSMibRevMinor=hpnsaRPSMibRevMinor, nm=nm, hpnsa=hpnsa, hpnsaRPS=hpnsaRPS)
