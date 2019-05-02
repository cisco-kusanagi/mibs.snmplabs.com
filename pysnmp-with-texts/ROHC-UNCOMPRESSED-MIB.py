#
# PySNMP MIB module ROHC-UNCOMPRESSED-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ROHC-UNCOMPRESSED-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:58:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rohcChannelID, rohcContextCID = mibBuilder.importSymbols("ROHC-MIB", "rohcChannelID", "rohcContextCID")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
mib_2, MibIdentifier, Counter64, NotificationType, Bits, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, iso, ModuleIdentity, Counter32, ObjectIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "MibIdentifier", "Counter64", "NotificationType", "Bits", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "iso", "ModuleIdentity", "Counter32", "ObjectIdentity", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rohcUncmprMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 113))
rohcUncmprMIB.setRevisions(('2004-06-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rohcUncmprMIB.setRevisionsDescriptions(('Initial version, published as RFC 3816.',))
if mibBuilder.loadTexts: rohcUncmprMIB.setLastUpdated('200406030000Z')
if mibBuilder.loadTexts: rohcUncmprMIB.setOrganization('IETF Robust Header Compression Working Group')
if mibBuilder.loadTexts: rohcUncmprMIB.setContactInfo('WG charter: http://www.ietf.org/html.charters/rohc-charter.html Mailing Lists: General Discussion: rohc@ietf.org To Subscribe: rohc-request@ietf.org In Body: subscribe your_email_address Editor: Juergen Quittek NEC Europe Ltd. Network Laboratories Kurfuersten-Anlage 36 69221 Heidelberg Germany Tel: +49 6221 90511-15 EMail: quittek@netlab.nec.de')
if mibBuilder.loadTexts: rohcUncmprMIB.setDescription('This MIB module defines a set of objects for monitoring and configuring RObust Header Compression (ROHC). The objects are specific to ROHC uncompressed (profile 0x0000). Copyright (C) The Internet Society (2004). The initial version of this MIB module was published in RFC 3816. For full legal notices see the RFC itself or see: http://www.ietf.org/copyrights/ianamib.html')
rohcUncmprObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 113, 1))
rohcUncmprConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 113, 2))
rohcUncmprContextTable = MibTable((1, 3, 6, 1, 2, 1, 113, 1, 1), )
if mibBuilder.loadTexts: rohcUncmprContextTable.setStatus('current')
if mibBuilder.loadTexts: rohcUncmprContextTable.setDescription('This table lists and describes ROHC uncompressed profile specific properties of compressor contexts and decompressor contexts. It extends the rohcContextTable of the ROHC-MIB module.')
rohcUncmprContextEntry = MibTableRow((1, 3, 6, 1, 2, 1, 113, 1, 1, 1), ).setIndexNames((0, "ROHC-MIB", "rohcChannelID"), (0, "ROHC-MIB", "rohcContextCID"))
if mibBuilder.loadTexts: rohcUncmprContextEntry.setStatus('current')
if mibBuilder.loadTexts: rohcUncmprContextEntry.setDescription('An entry describing a particular context.')
rohcUncmprContextState = MibTableColumn((1, 3, 6, 1, 2, 1, 113, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("initAndRefresh", 1), ("normal", 2), ("noContext", 3), ("fullContext", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rohcUncmprContextState.setReference('RFC 3095, Section 5.10.3')
if mibBuilder.loadTexts: rohcUncmprContextState.setStatus('current')
if mibBuilder.loadTexts: rohcUncmprContextState.setDescription('State of the context. States initAndRefresh(1) and normal(2) are states of compressor contexts, states noContext(3) and fullContext(4) are states of decompressor contexts.')
rohcUncmprContextMode = MibTableColumn((1, 3, 6, 1, 2, 1, 113, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unidirectional", 1), ("bidirectional", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rohcUncmprContextMode.setReference('RFC 3095, Section 5.10.3')
if mibBuilder.loadTexts: rohcUncmprContextMode.setStatus('current')
if mibBuilder.loadTexts: rohcUncmprContextMode.setDescription('Mode of the context.')
rohcUncmprContextACKs = MibTableColumn((1, 3, 6, 1, 2, 1, 113, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rohcUncmprContextACKs.setReference('RFC 3095, Section 5.2.1')
if mibBuilder.loadTexts: rohcUncmprContextACKs.setStatus('current')
if mibBuilder.loadTexts: rohcUncmprContextACKs.setDescription('The number of all positive feedbacks (ACK) sent or received in this context, respectively. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime. For checking ifCounterDiscontinuityTime, the interface index is required. It can be determined by reading the rohcChannelTable of the ROHC-MIB.')
rohcUncmprCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 113, 2, 1))
rohcUncmprGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 113, 2, 2))
rohcUncmprCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 113, 2, 1, 1)).setObjects(("ROHC-UNCOMPRESSED-MIB", "rohcUncmprContextGroup"), ("ROHC-UNCOMPRESSED-MIB", "rohcUncmprStatisticsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rohcUncmprCompliance = rohcUncmprCompliance.setStatus('current')
if mibBuilder.loadTexts: rohcUncmprCompliance.setDescription('The compliance statement for SNMP entities that implement the ROHC-UNCOMPRESSED-MIB. Note that compliance with this compliance statement requires compliance with the rohcCompliance MODULE-COMPLIANCE statement of the ROHC-MIB and with the ifCompliance3 MODULE-COMPLIANCE statement of the IF-MIB (RFC2863).')
rohcUncmprContextGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 113, 2, 2, 1)).setObjects(("ROHC-UNCOMPRESSED-MIB", "rohcUncmprContextState"), ("ROHC-UNCOMPRESSED-MIB", "rohcUncmprContextMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rohcUncmprContextGroup = rohcUncmprContextGroup.setStatus('current')
if mibBuilder.loadTexts: rohcUncmprContextGroup.setDescription('A collection of objects providing information about ROHC uncompressed compressors and decompressors.')
rohcUncmprStatisticsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 113, 2, 2, 2)).setObjects(("ROHC-UNCOMPRESSED-MIB", "rohcUncmprContextACKs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rohcUncmprStatisticsGroup = rohcUncmprStatisticsGroup.setStatus('current')
if mibBuilder.loadTexts: rohcUncmprStatisticsGroup.setDescription('An object providing context statistics.')
mibBuilder.exportSymbols("ROHC-UNCOMPRESSED-MIB", rohcUncmprMIB=rohcUncmprMIB, PYSNMP_MODULE_ID=rohcUncmprMIB, rohcUncmprCompliances=rohcUncmprCompliances, rohcUncmprCompliance=rohcUncmprCompliance, rohcUncmprContextEntry=rohcUncmprContextEntry, rohcUncmprStatisticsGroup=rohcUncmprStatisticsGroup, rohcUncmprObjects=rohcUncmprObjects, rohcUncmprContextACKs=rohcUncmprContextACKs, rohcUncmprConformance=rohcUncmprConformance, rohcUncmprGroups=rohcUncmprGroups, rohcUncmprContextState=rohcUncmprContextState, rohcUncmprContextMode=rohcUncmprContextMode, rohcUncmprContextGroup=rohcUncmprContextGroup, rohcUncmprContextTable=rohcUncmprContextTable)
