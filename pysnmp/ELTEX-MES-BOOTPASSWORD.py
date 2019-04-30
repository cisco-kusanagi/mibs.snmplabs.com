#
# PySNMP MIB module ELTEX-MES-BOOTPASSWORD (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-BOOTPASSWORD
# Produced by pysmi-0.3.4 at Mon Apr 29 18:46:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
eltMesDevParams, = mibBuilder.importSymbols("ELT-MES-DEV-PARAMS", "eltMesDevParams")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, iso, Counter64, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, Bits, ObjectIdentity, NotificationType, TimeTicks, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Counter64", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "Bits", "ObjectIdentity", "NotificationType", "TimeTicks", "Unsigned32", "IpAddress")
TruthValue, TextualConvention, DateAndTime, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DateAndTime", "DisplayString", "RowStatus")
eltMesBootPassword = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 2, 17))
eltMesBootPassword.setRevisions(('2012-12-14 00:00',))
if mibBuilder.loadTexts: eltMesBootPassword.setLastUpdated('201212140000Z')
if mibBuilder.loadTexts: eltMesBootPassword.setOrganization('Eltex Enterprise Co, Ltd.')
eltBootPasswordString = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 2, 17, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltBootPasswordString.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-BOOTPASSWORD", PYSNMP_MODULE_ID=eltMesBootPassword, eltBootPasswordString=eltBootPasswordString, eltMesBootPassword=eltMesBootPassword)
