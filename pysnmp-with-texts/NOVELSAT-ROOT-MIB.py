#
# PySNMP MIB module NOVELSAT-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NOVELSAT-ROOT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:24:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, enterprises, NotificationType, MibIdentifier, Bits, ModuleIdentity, TimeTicks, Gauge32, IpAddress, iso, Unsigned32, Counter32, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "enterprises", "NotificationType", "MibIdentifier", "Bits", "ModuleIdentity", "TimeTicks", "Gauge32", "IpAddress", "iso", "Unsigned32", "Counter32", "Integer32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nsRoot = ModuleIdentity((1, 3, 6, 1, 4, 1, 37576))
nsRoot.setRevisions(('2010-09-12 15:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: nsRoot.setRevisionsDescriptions(('Version 1.0.0.X',))
if mibBuilder.loadTexts: nsRoot.setLastUpdated('201009121500Z')
if mibBuilder.loadTexts: nsRoot.setOrganization('Novelsat')
if mibBuilder.loadTexts: nsRoot.setContactInfo("21 Ha'taasiya St., Ra'anana 43654,Israel -------------------------- Tel: +972-9-7889730 Fax: +972-9- e-mail: info@novelsat.com, support@novelsat.com http://www.novelsat.com -------------------------- ")
if mibBuilder.loadTexts: nsRoot.setDescription('Main novelsat global MIB')
nsMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 37576, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsMibVersion.setStatus('current')
if mibBuilder.loadTexts: nsMibVersion.setDescription('This parameter holds the current version of this propietary MIB.')
mibBuilder.exportSymbols("NOVELSAT-ROOT-MIB", nsRoot=nsRoot, PYSNMP_MODULE_ID=nsRoot, nsMibVersion=nsMibVersion)
