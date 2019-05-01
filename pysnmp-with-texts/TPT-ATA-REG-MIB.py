#
# PySNMP MIB module TPT-ATA-REG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPT-ATA-REG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:26:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, NotificationType, Gauge32, ModuleIdentity, TimeTicks, iso, Bits, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "Gauge32", "ModuleIdentity", "TimeTicks", "iso", "Bits", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tpt_reg, = mibBuilder.importSymbols("TIPPINGPOINT-REG-MIB", "tpt-reg")
tpt_ata_family = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 10)).setLabel("tpt-ata-family")
tpt_ata_family.setRevisions(('2016-05-25 18:54', '2015-07-30 17:35',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tpt_ata_family.setRevisionsDescriptions(('Updated copyright information. Minor MIB syntax fixes.', 'Initial MIB version.',))
if mibBuilder.loadTexts: tpt_ata_family.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_ata_family.setOrganization('Trend Micro, Inc.')
if mibBuilder.loadTexts: tpt_ata_family.setContactInfo('www.trendmicro.com')
if mibBuilder.loadTexts: tpt_ata_family.setDescription("Registration sub-tree for TippingPoint Advanced Threat Application (ATA) products. Copyright (C) 2016 Trend Micro Incorporated. All Rights Reserved. Trend Micro makes no warranty of any kind with regard to this material, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. Trend Micro shall not be liable for errors contained herein or for incidental or consequential damages in connection with the furnishing, performance, or use of this material. This document contains proprietary information, which is protected by copyright. No part of this document may be photocopied, reproduced, or translated into another language without the prior written consent of Trend Micro. The information is provided 'as is' without warranty of any kind and is subject to change without notice. The only warranties for Trend Micro products and services are set forth in the express warranty statements accompanying such products and services. Nothing herein should be construed as constituting an additional warranty. Trend Micro shall not be liable for technical or editorial errors or omissions contained herein. TippingPoint(R), the TippingPoint logo, and Digital Vaccine(R) are registered trademarks of Trend Micro. All other company and product names may be trademarks of their respective holders. All rights reserved. This document contains confidential information, trade secrets or both, which are the property of Trend Micro. No part of this documentation may be reproduced in any form or by any means or used to make any derivative work (such as translation, transformation, or adaptation) without written permission from Trend Micro or one of its subsidiaries. All other company and product names may be trademarks of their respective holders. ")
tpt_model_ata_network = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 10, 1)).setLabel("tpt-model-ata-network")
if mibBuilder.loadTexts: tpt_model_ata_network.setStatus('current')
if mibBuilder.loadTexts: tpt_model_ata_network.setDescription('Registration for TippingPoint ATA Network Appliances.')
tpt_model_ata_mail = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 10, 2)).setLabel("tpt-model-ata-mail")
if mibBuilder.loadTexts: tpt_model_ata_mail.setStatus('current')
if mibBuilder.loadTexts: tpt_model_ata_mail.setDescription('Registration for TippingPoint ATA Mail Appliances.')
mibBuilder.exportSymbols("TPT-ATA-REG-MIB", tpt_model_ata_mail=tpt_model_ata_mail, tpt_model_ata_network=tpt_model_ata_network, PYSNMP_MODULE_ID=tpt_ata_family, tpt_ata_family=tpt_ata_family)
