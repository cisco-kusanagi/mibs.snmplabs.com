#
# PySNMP MIB module RADLAN-SNA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-SNA-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:49:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter64, NotificationType, MibIdentifier, ObjectIdentity, Integer32, iso, IpAddress, Counter32, Unsigned32, Gauge32, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "NotificationType", "MibIdentifier", "ObjectIdentity", "Integer32", "iso", "IpAddress", "Counter32", "Unsigned32", "Gauge32", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TestAndIncr, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TestAndIncr", "TextualConvention")
rlSna = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 229))
rlSna.setRevisions(('2015-05-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlSna.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlSna.setLastUpdated('201101050000Z')
if mibBuilder.loadTexts: rlSna.setOrganization('Radlan - a MARVELL company. Marvell Semiconductor, Inc.')
if mibBuilder.loadTexts: rlSna.setContactInfo('www.marvell.com')
if mibBuilder.loadTexts: rlSna.setDescription('This private MIB module is used for communication between SNA client and SNA server.')
rlSnaNextFreeSessionId = MibScalar((1, 3, 6, 1, 4, 1, 89, 229, 1), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSnaNextFreeSessionId.setStatus('current')
if mibBuilder.loadTexts: rlSnaNextFreeSessionId.setDescription('The MIB allows several SNA clients operating at the same time to receive different session ids. Get operation on this MIB will return the next free session id number. An SNA client should then issue SET operation with the value it received. The response will be one of the following: - noError. - inconsistentValue in case another client has already used this session id. - resourceUnavailable in case the number of active sessions has already reached the maximum. In case of success, a new session events database is allocated for the session id.')
mibBuilder.exportSymbols("RADLAN-SNA-MIB", rlSnaNextFreeSessionId=rlSnaNextFreeSessionId, rlSna=rlSna, PYSNMP_MODULE_ID=rlSna)
