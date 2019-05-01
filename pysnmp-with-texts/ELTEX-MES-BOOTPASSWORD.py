#
# PySNMP MIB module ELTEX-MES-BOOTPASSWORD (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-BOOTPASSWORD
# Produced by pysmi-0.3.4 at Wed May  1 13:00:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
eltMesDevParams, = mibBuilder.importSymbols("ELT-MES-DEV-PARAMS", "eltMesDevParams")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Counter64, IpAddress, TimeTicks, Unsigned32, ModuleIdentity, Integer32, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Counter64", "IpAddress", "TimeTicks", "Unsigned32", "ModuleIdentity", "Integer32", "iso", "NotificationType")
TruthValue, DateAndTime, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DateAndTime", "RowStatus", "TextualConvention", "DisplayString")
eltMesBootPassword = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 2, 17))
eltMesBootPassword.setRevisions(('2012-12-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eltMesBootPassword.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: eltMesBootPassword.setLastUpdated('201212140000Z')
if mibBuilder.loadTexts: eltMesBootPassword.setOrganization('Eltex Enterprise Co, Ltd.')
if mibBuilder.loadTexts: eltMesBootPassword.setContactInfo('www.eltex.nsk.ru')
if mibBuilder.loadTexts: eltMesBootPassword.setDescription("This private MIB module defines Eltex's private MIBs.")
eltBootPasswordString = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 2, 17, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltBootPasswordString.setStatus('current')
if mibBuilder.loadTexts: eltBootPasswordString.setDescription('Specifies boot-menu password string. ')
mibBuilder.exportSymbols("ELTEX-MES-BOOTPASSWORD", PYSNMP_MODULE_ID=eltMesBootPassword, eltBootPasswordString=eltBootPasswordString, eltMesBootPassword=eltMesBootPassword)
