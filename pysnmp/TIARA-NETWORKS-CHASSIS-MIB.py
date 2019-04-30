#
# PySNMP MIB module TIARA-NETWORKS-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIARA-NETWORKS-CHASSIS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:09:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, NotificationType, Integer32, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, TimeTicks, ObjectIdentity, Bits, Gauge32, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Integer32", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "Bits", "Gauge32", "Unsigned32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tiaraMgmt, = mibBuilder.importSymbols("TIARA-NETWORKS-SMI", "tiaraMgmt")
tiaraChassisMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3174, 2, 2))
tiaraChassisMib.setRevisions(('1900-01-27 00:00',))
if mibBuilder.loadTexts: tiaraChassisMib.setLastUpdated('0001270000Z')
if mibBuilder.loadTexts: tiaraChassisMib.setOrganization('Tiara Networks, Inc.')
chassisType = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisType.setStatus('current')
chassisSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisSerialNumber.setStatus('current')
mibBuilder.exportSymbols("TIARA-NETWORKS-CHASSIS-MIB", PYSNMP_MODULE_ID=tiaraChassisMib, chassisSerialNumber=chassisSerialNumber, chassisType=chassisType, tiaraChassisMib=tiaraChassisMib)
