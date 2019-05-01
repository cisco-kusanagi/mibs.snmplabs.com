#
# PySNMP MIB module CISCO-VOICE-APPLICATIONS-OID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VOICE-APPLICATIONS-OID-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:19:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ciscoModules, = mibBuilder.importSymbols("CISCO-SMI", "ciscoModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, MibIdentifier, Integer32, iso, Bits, Counter64, Gauge32, IpAddress, TimeTicks, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "Integer32", "iso", "Bits", "Counter64", "Gauge32", "IpAddress", "TimeTicks", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoVoiceApplicationsOIDMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 12, 5))
ciscoVoiceApplicationsOIDMIB.setRevisions(('2004-06-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVoiceApplicationsOIDMIB.setRevisionsDescriptions(('The initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVoiceApplicationsOIDMIB.setLastUpdated('200406170000Z')
if mibBuilder.loadTexts: ciscoVoiceApplicationsOIDMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVoiceApplicationsOIDMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-itm@cisco.com')
if mibBuilder.loadTexts: ciscoVoiceApplicationsOIDMIB.setDescription('This module defines the object identifiers that are assigned to various Cisco voice applications. Voice applications include call agents and other voice application products. Call agents are call processing components of a device in a IP telephony and VoIP network.')
cvaMIBOids = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 5, 1))
ciscoCallManager = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 5, 1, 1))
ciscoCallManagerExpress = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 5, 1, 2))
ciscoSRST = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 5, 1, 3))
ciscoBTS = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 5, 1, 4))
ciscoCSPS = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 5, 1, 5))
mibBuilder.exportSymbols("CISCO-VOICE-APPLICATIONS-OID-MIB", ciscoCSPS=ciscoCSPS, ciscoCallManager=ciscoCallManager, ciscoCallManagerExpress=ciscoCallManagerExpress, PYSNMP_MODULE_ID=ciscoVoiceApplicationsOIDMIB, ciscoBTS=ciscoBTS, ciscoSRST=ciscoSRST, ciscoVoiceApplicationsOIDMIB=ciscoVoiceApplicationsOIDMIB, cvaMIBOids=cvaMIBOids)
