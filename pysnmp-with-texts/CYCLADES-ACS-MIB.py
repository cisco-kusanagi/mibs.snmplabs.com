#
# PySNMP MIB module CYCLADES-ACS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CYCLADES-ACS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:34:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
cyclades, = mibBuilder.importSymbols("CYCLADES-MIB", "cyclades")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, TimeTicks, IpAddress, MibIdentifier, Bits, ObjectIdentity, Counter32, ModuleIdentity, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "TimeTicks", "IpAddress", "MibIdentifier", "Bits", "ObjectIdentity", "Counter32", "ModuleIdentity", "NotificationType", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cyACSMgmt = ModuleIdentity((1, 3, 6, 1, 4, 1, 2925, 4))
cyACSMgmt.setRevisions(('2005-08-29 00:00', '2003-10-17 00:00', '2002-10-10 00:00', '2002-09-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cyACSMgmt.setRevisionsDescriptions(('Changed the Contact-Info', 'Defined new MIB - CYCLADES-ACS-PM-MIB', 'Defined new MIB - CYCLADES-ACS-SYS-MIB', 'First Draft',))
if mibBuilder.loadTexts: cyACSMgmt.setLastUpdated('200508290000Z')
if mibBuilder.loadTexts: cyACSMgmt.setOrganization('Cyclades Corporation')
if mibBuilder.loadTexts: cyACSMgmt.setContactInfo('postal : Cyclades Corporation 3541 Gateway Boulevard Fremont, CA 94538, USA e-mail : Technical Support support@cyclades.com')
if mibBuilder.loadTexts: cyACSMgmt.setDescription('This file defines the Cyclades MIB extensions to ACSxx products')
mibBuilder.exportSymbols("CYCLADES-ACS-MIB", PYSNMP_MODULE_ID=cyACSMgmt, cyACSMgmt=cyACSMgmt)
