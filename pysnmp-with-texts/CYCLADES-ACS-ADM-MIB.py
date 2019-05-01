#
# PySNMP MIB module CYCLADES-ACS-ADM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CYCLADES-ACS-ADM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:34:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
cyACSMgmt, = mibBuilder.importSymbols("CYCLADES-ACS-MIB", "cyACSMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, TimeTicks, IpAddress, MibIdentifier, Bits, ObjectIdentity, Counter32, ModuleIdentity, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "TimeTicks", "IpAddress", "MibIdentifier", "Bits", "ObjectIdentity", "Counter32", "ModuleIdentity", "NotificationType", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cyACSAdm = ModuleIdentity((1, 3, 6, 1, 4, 1, 2925, 4, 4))
cyACSAdm.setRevisions(('2005-08-29 00:00', '2002-09-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cyACSAdm.setRevisionsDescriptions(('Changed the Contact-Info', 'First Draft',))
if mibBuilder.loadTexts: cyACSAdm.setLastUpdated('200508290000Z')
if mibBuilder.loadTexts: cyACSAdm.setOrganization('Cyclades Corporation')
if mibBuilder.loadTexts: cyACSAdm.setContactInfo('postal : Cyclades Corporation 3541 Gateway Boulevard Fremont, CA 94538, USA e-mail : Technical Support support@cyclades.com')
if mibBuilder.loadTexts: cyACSAdm.setDescription('This module defines objects of the ACS/TS administration')
cyACSSave = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("nosave", 0), ("save", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyACSSave.setStatus('current')
if mibBuilder.loadTexts: cyACSSave.setDescription('Exec saveconf command')
cyACSSerialHUP = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("norestartportslave", 0), ("restartportslave", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyACSSerialHUP.setStatus('current')
if mibBuilder.loadTexts: cyACSSerialHUP.setDescription('Exec signal_ras hup command')
mibBuilder.exportSymbols("CYCLADES-ACS-ADM-MIB", cyACSAdm=cyACSAdm, cyACSSave=cyACSSave, cyACSSerialHUP=cyACSSerialHUP, PYSNMP_MODULE_ID=cyACSAdm)
