#
# PySNMP MIB module SONICWALL-SSL (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONICWALL-SSL
# Produced by pysmi-0.3.4 at Wed May  1 15:09:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, Integer32, Counter32, Gauge32, Unsigned32, ObjectIdentity, MibIdentifier, IpAddress, iso, TimeTicks, NotificationType, NotificationType, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "Integer32", "Counter32", "Gauge32", "Unsigned32", "ObjectIdentity", "MibIdentifier", "IpAddress", "iso", "TimeTicks", "NotificationType", "NotificationType", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sonicWALL = MibIdentifier((1, 3, 6, 1, 4, 1, 8714))
sonicSEC = ModuleIdentity((1, 3, 6, 1, 4, 1, 8714, 2))
if mibBuilder.loadTexts: sonicSEC.setLastUpdated('200203061330Z')
if mibBuilder.loadTexts: sonicSEC.setOrganization('SonicWALL, Inc.')
if mibBuilder.loadTexts: sonicSEC.setContactInfo(' SonicWall Inc. Postal: 1160 Bordeaux Dr. Sunnyvale, CA 94089 USA Tel: +1 408 745 9600 Fax: +1 408 745 9300 E-mail: support@sonicwall.com')
if mibBuilder.loadTexts: sonicSEC.setDescription('The MIB module for SonicWALL enterprise security devices.')
mibBuilder.exportSymbols("SONICWALL-SSL", sonicSEC=sonicSEC, PYSNMP_MODULE_ID=sonicSEC, sonicWALL=sonicWALL)
